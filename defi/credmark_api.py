import requests
import json 
import time 
import pandas as pd
import os

# using python-dotenv method
from dotenv import load_dotenv
load_dotenv()

# authorization & header
auth_token = os.environ.get('AUTH_TOKEN')
HEADER = {'Authorization': 'Bearer ' + f'{auth_token}'}


# --- Token API Data Endpoints

weth_name = requests.get('https://gateway.credmark.com/v1/tokens/1/0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2/name', headers=HEADER)
weth_symbol = requests.get('https://gateway.credmark.com/v1/tokens/1/0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2/symbol', headers=HEADER)
weth_logo = requests.get('https://gateway.credmark.com/v1/tokens/1/0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2/logo', headers=HEADER)

curve = requests.get('https://gateway.credmark.com/v1/tokens/1/0xdF5e0e81Dff6FAF3A7e52BA697820c5e32D806A8/name', headers=HEADER)

frax_price = requests.get('https://gateway.credmark.com/v1/tokens/1/0x853d955aCEf822Db058eb8505911ED77F175b99e/price', headers=HEADER)

print(weth_name.json())
print(weth_symbol.json())
print(weth_logo.json())

print(curve.json())
print(frax_price.json())

# could not find token abi

# --- DeFi API Data Endpoints

# balancer model metadata by slug
#balancer = requests.get('https://gateway.credmark.com/v1/models/balancer-fi.get-all-pools', headers=HEADER)

#print(balancer.json())

# --- Utilities

#usage = requests.get('https://gateway.credmark.com/v1/usage/top', headers=HEADER)
#print(usage.json())