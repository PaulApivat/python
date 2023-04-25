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
phishing = df[df['ADDRESS_NAME'].str.contains("phishing", na=False)]
non_phishing = df[df['ADDRESS_NAME'].str.contains("phishing") == False]

# Compute ppdeep hashes for the 'BYTECODE' column of phishing data
phishing_hashes = phishing['BYTECODE'].apply(ppdeep.hash)

# add phishing_hashes to phishing df, then  create a duplicate 
phishing['PPDEEP_1'] = phishing_hashes
phishing['PPDEEP_2'] = phishing.loc[:, 'PPDEEP_1']

# Compute pairwise similarity scores for the phishing hashes, remove duplicates
phishing_pairs = set(itertools.permutations(phishing_hashes, 2))
phishing_similarities = [(pair[0] + "," + pair[1], ppdeep.compare(pair[0], pair[1])) for pair in phishing_pairs]
phishing_similarities = [(pair, score) for pair, score in phishing_similarities if score > 0]

# Join the phishing data with the similarity scores
phishing_pair_similar_df = pd.DataFrame(phishing_similarities, columns=['hashed pair', 'similarity score'])
phishing_pair_similar_df[['PPDEEP_1', 'PPDEEP_2']] = phishing_pair_similar_df['hashed pair'].str.split(',', expand=True)
merged_df = phishing_pair_similar_df.merge(phishing, on='PPDEEP_1', how='left', indicator=True)
merged_df_2 = phishing_pair_similar_df.merge(phishing, on='PPDEEP_2', how='left', indicator=True)


# Select the relevant columns and return the result as a dictionary
phishing_pair_similar = {
    'similarity': merged_df['similarity score'],
    'hash_1': merged_df['PPDEEP_1'],
    'hash_2': merged_df['PPDEEP_2_x'],
    'address_1': merged_df['CONTRACT_ADDRESS'],
    'address_2': merged_df_2['CONTRACT_ADDRESS'],
    'label_1': merged_df['ADDRESS_NAME'],
    'label_2': merged_df_2['ADDRESS_NAME']
}

phishing_pair_similar_df = pd.DataFrame(phishing_pair_similar)
print(phishing_pair_similar_df)

