import requests
import json 
import time 
import pandas as pd
import os

# using python-dotenv method
from dotenv import load_dotenv
load_dotenv()

address1 = "0xddbd2b932c763ba5b1b7ae3b362eac3e8d40121a"
address2 = "0x63a9975ba31b0b9626b34300f7f627147df1f526"
address3 = "0x198ef1ec325a96cc354c7266a038be8b5c558f67"

# etherscan key
eskey = os.environ.get('ETHERSCANKEY')

res = requests.get(f"https://api.etherscan.io/api?module=account&action=balancemulti&address={address1}, {address2}, {address3}&tag=latest&apikey={eskey}")

# response 200
print(res)
print(res.json())