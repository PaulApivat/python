import sqlalchemy
import psycopg2
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

usdc_supply = requests.get('https://gateway.credmark.com/v1/tokens/1/0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48/total-supply', headers=header)
usdt_supply = requests.get('https://gateway.credmark.com/v1/tokens/1/0xdAC17F958D2ee523a2206206994597C13D831ec7/total-supply', headers=header)
busd_supply = requests.get('https://gateway.credmark.com/v1/tokens/1/0x4Fabb145d64652a948d72533023f6E7A623C7C53/total-supply', headers=header)
dai_supply = requests.get('https://gateway.credmark.com/v1/tokens/1/0x6B175474E89094C44Da98b954EedeAC495271d0F/total-supply', headers=header)
lusd_supply = requests.get('https://gateway.credmark.com/v1/tokens/1/0x5f98805A4E8be255a32880FDeC7F6728C6568bA0/total-supply', headers=header)
frax_supply = requests.get('https://gateway.credmark.com/v1/tokens/1/0x853d955aCEf822Db058eb8505911ED77F175b99e/total-supply', headers=header)

# --- convert dict to dataframe

usdc_dict = usdc_supply.json()
usdt_dict = usdt_supply.json()
busd_dict = busd_supply.json()
dai_dict = dai_supply.json()
lusd_dict = lusd_supply.json()
frax_dict = frax_supply.json()

stable_df = pd.DataFrame([usdc_dict, usdt_dict, busd_dict, dai_dict, lusd_dict, frax_dict])

print(stable_df)
print(stable_df.dtypes)

# --- load dataframe to postgres db

# reference python-dotenv method above
db_user = os.environ.get('DB_USER')
db_password = os.environ.get('DB_PASSWORD')

# database connection string
db_string = f'postgresql://{db_user}:{db_password}@localhost:5432/credmark'
db = create_engine(db_string)
conn = db.connect()

print(db)
print(conn)


# insert: dataframe to sql
stable_df.to_sql('stablecoins', con=db, if_exists='replace', index=False)

# read data
result_set = db.execute("SELECT * FROM stablecoins")

for r in result_set:
    print(r)

