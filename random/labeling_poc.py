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

print("Number of rows for phishing df: ", len(phishing['BYTECODE'].index))
print("Nunber of row for non_phishing df: ", len(non_phishing['BYTECODE'].index))

print("Index for phishing df: ", phishing['BYTECODE'].index)
print("Index for non_phishing df: ", non_phishing['BYTECODE'].index)


"""
Index for phishing df:  Index([  0,   9,  24,  29,  30,  33,  35,  50,  51,  52,  73,  78,  79,  84,
       112, 113, 123, 125, 127, 128, 136, 143, 144, 149, 154, 155, 162, 171,
       178, 179, 183, 184, 185, 186, 188, 192, 197, 203, 205, 207, 222, 226,
       227, 231, 238, 253, 270, 298, 301, 311],
      dtype='int64')

Index for non_phishing df:  Index([  1,   2,   3,   4,   5,   6,   7,   8,  10,  11,
       ...
       300, 302, 303, 304, 305, 306, 307, 308, 309, 310],
      dtype='int64', length=262)


Hypothesis: two phishing indices (0, 9) and two non_phishing indices (1, 2) should have higher similarity within group than between group     *
Hypothesis: two phishing indices (24, 29) and two non_phishing indices (3, 4) should have higher similarity within group than between group   *
Hypothesis: two phishing indices (30, 33) and two non_phishing indices (5, 6) should have higher similarity within group than between group   x
Hypothesis: two phishing indices (35, 50) and two non_phishing indices (7, 8) should have higher similarity within group than between group   x
Hypothesis: two phishing indices (51, 52) and two non_phishing indices (10, 11) should have higher similarity within group than between group   x
Hypothesis: two phishing indices (73, 78) and two non_phishing indices (300, 302) should have higher similarity within group than between group  *
"""

phishing_1 = ppdeep.hash(phishing['BYTECODE'][73])
phishing_2 = ppdeep.hash(phishing['BYTECODE'][78])

non_phishing_1 = ppdeep.hash(non_phishing['BYTECODE'][300])
non_phishing_2 = ppdeep.hash(non_phishing['BYTECODE'][302])

print("phishing_1: ", phishing_1)
print("phishing_2: ", phishing_2)
print("non_phishing_1: ", non_phishing_1)
print("non_phishing_2: ", non_phishing_2)

compare_phishing = ppdeep.compare(phishing_1, phishing_2)
compare_non_phishing = ppdeep.compare(non_phishing_1, non_phishing_2)

compare_btwn_group_1 = ppdeep.compare(phishing_1, non_phishing_1)
compare_btwn_group_2 = ppdeep.compare(phishing_1, non_phishing_2)
compare_btwn_group_3 = ppdeep.compare(phishing_2, non_phishing_1)
compare_btwn_group_4 = ppdeep.compare(phishing_2, non_phishing_2)

print("compare_phishing: ", compare_phishing)
print("compare_non_phishing: ", compare_non_phishing)
print("compare_btwn_group_1: ", compare_btwn_group_1)
print("compare_btwn_group_2: ", compare_btwn_group_2)
print("compare_btwn_group_3: ", compare_btwn_group_3)
print("compare_btwn_group_4: ", compare_btwn_group_4)


"""
Loop through phishing and non_phishing columns
Take every permutation of all pairs, except duplicates
Run each pair through ppdeep.compare() to get similarity scores
Rank order similarity score column

** Need a way to connect "hash pairs" with individual smart contract address. 
"""





# loop through phishing['BYTECODE']
phishing_list = list()

for i in phishing['BYTECODE'].index:
      phishing_list.append(ppdeep.hash(phishing['BYTECODE'][i]))
      print("all phishing hashes inserted.")

# add phishing_list into phishing df
phishing['PPDEEP_1'] = phishing_list

phishing['PPDEEP_2'] = phishing.loc[:, 'PPDEEP_1']

#compare_phishing_list = [ppdeep.compare(p1, p2) for p1 in phishing_list for p2 in phishing_list]

# loop through phishing_list, take each pair, excluding duplicates
# put each unique pair through ppdeep.compare() to find similarity score
# place each hashed pair and similarity score in a tuple
compare_phishing_list = list()

"""
for x in phishing_list:
      for y in phishing_list:
            if x != y:
                  compare_phishing_list.append((x + " & " + y, ppdeep.compare(x, y)))
"""

for x in phishing['PPDEEP_1']:
      for y in phishing['PPDEEP_1']:
            if x != y:
                  compare_phishing_list.append((x + "," + y, ppdeep.compare(x, y)))

# Convert list of tuple to dataframe with two new columns
# rank order 'similarity score' column in descending order by similarity score
# The idea is to go back to the pair of addresses for each pair that had a high similarity score and see if contract names are similar
phishing_df = pd.DataFrame(compare_phishing_list, columns = ['hashed pair', 'similarity score'])

phishing_df_sorted = phishing_df.sort_values('similarity score', ascending=False)

phishing_df_high_similar = phishing_df[phishing_df['similarity score'] > 0]

#phishing_df_high_similar.to_csv("phishing_df_high_similar")

phishing_df_high_similar[['PPDEEP_1', 'PPDEEP_2']] = phishing_df_high_similar['hashed pair'].str.split(',', expand=True)

print(phishing_df_high_similar)

merged_df = phishing_df_high_similar.merge(phishing, on='PPDEEP_1', how='left', indicator=True)

merged_df_2 = phishing_df_high_similar.merge(phishing, on='PPDEEP_2', how='left', indicator=True)

"""
check merged_df.columns, merged_df_2.columns
check for CONTRACT_ADDRESS pair associted with ppdeep hashed pair
manually check contract address pair (with high similarity) in etherscan 

merged_df['CONTRACT_ADDRESS'] -- address 1
merged_df_2['CONTRACT_ADDRESS'] -- address 2


note: 
merged_df['PPDEEP_1'] == merged_df_2['PPDEEP_1_x']
merged_df_2['PPDEEP_2'] == merged_df['PPDEEP_2_x']

create new df

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
"""

