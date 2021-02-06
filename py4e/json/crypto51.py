# coding: utf-8
import pandas as pd
import json
import requests

r = requests.get('https://api.crypto51.app/coins.json')

type(r.json())

dct = dict()

dct = r.json()

print(dct)

# exploring dct

# dict
type(dct)

# loop through:
# last_updated
# coins
for x, y in dct.items():
    print(x)

# list
type(dct['coins'])
len(dct['coins'])  # 57 dictionaries in side this list

# convert list of 57 dictionaries into a pandas dataframe


df = pd.DataFrame.from_dict(dct['coins'])

df.head()

# df.to_csv('crypto51.csv', index=False)
