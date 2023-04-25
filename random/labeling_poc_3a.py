import requests
import pandas as pd
import ppdeep
import itertools

import os
from dotenv import load_dotenv
load_dotenv()

# URL of the API endpoint
url = os.environ.get('FLIPSIDE_API')

# Send a GET request to the URL
response = requests.get(url)
if not response.ok:
    raise Exception(f"Failed to fetch data from {url}. Status code: {response.status_code}")

# Parse the response as JSON
data = response.json()

# Convert the data to a DataFrame
df = pd.DataFrame(data)

# Split the data into phishing and non-phishing based on the 'ADDRESS_NAME' column
#phishing = df[df['ADDRESS_NAME'].str.contains("phishing", na=False)]
non_phishing = df[df['ADDRESS_NAME'].str.contains("phishing") == False]

# Compute ppdeep hashes for the 'BYTECODE' column of non_phishing data
non_phishing_hashes = non_phishing['BYTECODE'].apply(ppdeep.hash)

# add phishing_hashes to phishing df, then  create a duplicate 
non_phishing['PPDEEP_1'] = non_phishing_hashes
non_phishing['PPDEEP_2'] = non_phishing.loc[:, 'PPDEEP_1']

# Compute pairwise similarity scores for the phishing hashes, remove duplicates
non_phishing_pairs = set(itertools.permutations(non_phishing_hashes, 2))
non_phishing_similarities = [(pair[0] + "," + pair[1], ppdeep.compare(pair[0], pair[1])) for pair in non_phishing_pairs]
non_phishing_similarities = [(pair, score) for pair, score in non_phishing_similarities if score > 0]

# Join the phishing data with the similarity scores
non_phishing_pair_similar_df = pd.DataFrame(non_phishing_similarities, columns=['hashed pair', 'similarity score'])
non_phishing_pair_similar_df[['PPDEEP_1', 'PPDEEP_2']] = non_phishing_pair_similar_df['hashed pair'].str.split(',', expand=True)
merged_df = non_phishing_pair_similar_df.merge(non_phishing, on='PPDEEP_1', how='left', indicator=True)
merged_df_2 = non_phishing_pair_similar_df.merge(non_phishing, on='PPDEEP_2', how='left', indicator=True)


# Select the relevant columns and return the result as a dictionary
non_phishing_pair_similar = {
    'similarity': merged_df['similarity score'],
    'hash_1': merged_df['PPDEEP_1'],
    'hash_2': merged_df['PPDEEP_2_x'],
    'address_1': merged_df['CONTRACT_ADDRESS'],
    'address_2': merged_df_2['CONTRACT_ADDRESS'],
    'label_1': merged_df['ADDRESS_NAME'],
    'label_2': merged_df_2['ADDRESS_NAME']
}

non_phishing_pair_similar_df = pd.DataFrame(non_phishing_pair_similar)
print(non_phishing_pair_similar_df)