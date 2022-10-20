from sqlalchemy import create_engine
import requests
import json
import pprint 
import pandas as pd 
import os

# using python-dotenv method
from dotenv import load_dotenv
load_dotenv()

# authorization & header
auth_token = os.environ.get('AUTH_TOKEN')
header = {
    'Authorization': 'Bearer ' + f'{auth_token}',
    'Content-Type': 'application/json'
}

# --- Stable Coin Supply - Mkt Share
#usdc_supply = requests.get('https://gateway.credmark.com/v1/tokens/1/0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48/total-supply', headers=header)
#usdc_supply_ts = requests.get('https://gateway.credmark.com/v1/tokens/1/0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48/total-supply?start=1666232000&end=1666232999', headers=header)


# --- convert dict to dataframe

#usdc_dict = usdc_supply.json()
#usdc_dict_ts = usdc_supply_ts.json()

#print(usdc_dict)

# authorization & header
auth_token_new = os.environ.get('AUTH_TOKEN_NEW')

headers = {
    'Authorization': 'Bearer ' + f'{auth_token_new}',
    'Content-Type': 'application/json'
}


"""
# Curve Metapool (LUSD-3CRV); 
# Historical Distribution of LP Holders for a given pool

payload = {
  "slug": "curve-fi.historical-lp-dist",
  "chainId": 1,
  "blockNumber": "latest",
  "input": {
    "address": "0xEd279fDD11cA84bEef15AF5D39BB4d4bEE23F0cA"
  }
}

"""

# Curve Metapool (LUSD-3CRV); 
# Historical Distribution of LP Holders for a given pool
payload = {
  "slug": "series.block-start-end-interval",
  "chainId": 1,
  "blockNumber": "latest",
  "input": {
    "start": 14234000,
    "end": 14234900,
    "interval": 100
  }
}

series = requests.post('https://gateway.credmark.com/v1/model/run#series.block-start-end-interval', headers=headers, data=json.dumps(payload))

print(series.status_code)

pprint.pprint(series.json())