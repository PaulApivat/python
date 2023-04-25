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
print(response)

data = response.json()


df = pd.DataFrame(data)
phishing = df[df['ADDRESS_NAME'].str.contains("phishing", na = False)]
non_phishing = df[df['ADDRESS_NAME'].str.contains("phishing") == False]

# create empty list
phishing_list = list()

# loop through column, run row values through ppdeep.hash, append to empty list
for i in phishing['BYTECODE'].index:
      phishing_list.append(ppdeep.hash(phishing['BYTECODE'][i]))
      print("all phishing hashes inserted.")

# add phishing_list of bytecode hashes to create new column
phishing['PPDEEP_1'] = phishing_list
# duplicate new column
phishing['PPDEEP_2'] = phishing.loc[:, 'PPDEEP_1']

# create empty list
compare_phishing_list = list()

# loop through column, take every pair of hashes and compare them with the ppdeep.compare() function
# take every pair permutation, excluding duplicates
for x in phishing['PPDEEP_1']:
      for y in phishing['PPDEEP_1']:
            if x != y:
                  compare_phishing_list.append((x + "," + y, ppdeep.compare(x, y)))

# create new dataframe of hashed pair and similarity score
phishing_df = pd.DataFrame(compare_phishing_list, columns = ['hashed pair', 'similarity score'])
# filter for pairs that have similarity scores above 0
phishing_df_high_similar = phishing_df[phishing_df['similarity score'] > 0]
# split hashed pair column into two columns 
phishing_df_high_similar[['PPDEEP_1', 'PPDEEP_2']] = phishing_df_high_similar['hashed pair'].str.split(',', expand=True)


# join phishing_df_high_similar with phishing dataframe
merged_df = phishing_df_high_similar.merge(phishing, on='PPDEEP_1', how='left', indicator=True)
merged_df_2 = phishing_df_high_similar.merge(phishing, on='PPDEEP_2', how='left', indicator=True)

# create new dictionary from both merged_df and merged_df_2
phishing_pair_similar = {
      'similarity': merged_df['similarity score'],
      'hash_1': merged_df['PPDEEP_1'],
      'hash_2': merged_df['PPDEEP_2_x'],
      'address_1': merged_df['CONTRACT_ADDRESS'],
      'address_2': merged_df_2['CONTRACT_ADDRESS'],
      'label_1': merged_df['ADDRESS_NAME'],
      'label_2': merged_df_2['ADDRESS_NAME']
}

# convert dictionary to dataframe
phishing_pair_similar_df = pd.DataFrame(phishing_pair_similar)
# print dataframe
print(phishing_pair_similar_df)
