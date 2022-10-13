from urllib import request
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
#weth_name = requests.get('https://gateway.credmark.com/v1/tokens/1/0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2/name', headers=HEADER)


#weth_symbol = requests.get('https://gateway.credmark.com/v1/tokens/1/0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2/symbol', headers=HEADER)
#weth_logo = requests.get('https://gateway.credmark.com/v1/tokens/1/0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2/logo', headers=HEADER)
#curve = requests.get('https://gateway.credmark.com/v1/tokens/1/0xdF5e0e81Dff6FAF3A7e52BA697820c5e32D806A8/name', headers=HEADER)
#frax_price = requests.get('https://gateway.credmark.com/v1/tokens/1/0x853d955aCEf822Db058eb8505911ED77F175b99e/price', headers=HEADER)

#print(weth_name.json())
#print(weth_symbol.json())
#print(weth_logo.json())
#print(curve.json())
#print(frax_price.json())

# could not find token abi

# --- Stable Coin Supply - Mkt Share
usdc_supply = requests.get('https://gateway.credmark.com/v1/tokens/1/0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48/total-supply', headers=HEADER)
usdt_supply = requests.get('https://gateway.credmark.com/v1/tokens/1/0xdAC17F958D2ee523a2206206994597C13D831ec7/total-supply', headers=HEADER)
busd_supply = requests.get('https://gateway.credmark.com/v1/tokens/1/0x4Fabb145d64652a948d72533023f6E7A623C7C53/total-supply', headers=HEADER)
dai_supply = requests.get('https://gateway.credmark.com/v1/tokens/1/0x6B175474E89094C44Da98b954EedeAC495271d0F/total-supply', headers=HEADER)
lusd_supply = requests.get('https://gateway.credmark.com/v1/tokens/1/0x5f98805A4E8be255a32880FDeC7F6728C6568bA0/total-supply', headers=HEADER)
frax_supply = requests.get('https://gateway.credmark.com/v1/tokens/1/0x853d955aCEf822Db058eb8505911ED77F175b99e/total-supply', headers=HEADER)


print(usdc_supply.json())
print(usdt_supply.json())
print(busd_supply.json())
print(dai_supply.json())
print(lusd_supply.json())
print(frax_supply.json())

#aave_token = requests.get('https://gateway.credmark.com/v1/tokens/1/0x7fc66500c84a76ad7e9c93437bfc5ac33e2ddae9/price?quoteAddress=0x00000000000000000000000000000000000003d2&blockNumber=15000000', headers=HEADER)
#print(aave_token.json())

# --- DeFi API Data Endpoints

# balancer model metadata by slug
#balancer = requests.get('https://gateway.credmark.com/v1/models/balancer-fi.get-all-pools', headers=HEADER)

#print(balancer.json())

# --- Utilities

#usage = requests.get('https://gateway.credmark.com/v1/usage/top', headers=HEADER)
#print(usage.json())

# ---- Curve Pool Info
"""

payload = {
  "slug": "curve-fi.pool-info",
  "chainId": 1,
  "blockNumber": "latest",
  "input": {
    "address": "0xEd279fDD11cA84bEef15AF5D39BB4d4bEE23F0cA"
  }
}

curve_pool = requests.post('https://gateway.credmark.com/v1/model/run#curve-fi.pool-info', headers=HEADER, data=json.dumps(payload))

print(curve_pool.json())

#curve_pool = requests.post('https://gateway.credmark.com/v1/model/run#curve-fi.pool-info', data=payload)

"""