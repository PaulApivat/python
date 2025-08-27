import requests
import json
import pandas as pd

# URL for the GET request
# url = "https://api.llama.fi/protocol/aerodrome"
url = "https://api.llama.fi/protocol/pancakeswap"

# Making the GET request
response = requests.get(url)
data = json.loads(response.text)

# Checking the response status and printing the result
if response.status_code == 200:
    # Response is successful, return json keys
    # response.json() provides too large a blob
    print("Success! \n\nHere are the keys: \n\n", data.keys())
else:
    # Response failed
    print(f"Failed to retrieve data. Status code: {response.status_code}")


def explore_keys(obj, path=""):
    if isinstance(obj, dict):
        for key, value in obj.items():
            print(path + "." + key if path else key)
    elif isinstance(obj, list) and obj:
        explore_keys(obj[0], path + "[]")


explore_keys(data)

print("\n")
print("chain TVLs :", data["chainTvls"].keys())
print("\n")
print("Current Chain TVLs :", data["currentChainTvls"].keys())


# for chain, value in data["chainTvls"].items():
#     print(f"\nChain: {chain}")
#     if isinstance(value, dict):
#         first_key = next(iter(value))
#         print(f"First key: {first_key}, Value: {value[first_key]}")
#     elif isinstance(value, list) and value:
#         print(f"First value: {value[0]}")
#     else:
#         print("No values found.")

chain_dfs = {}

for chain, value in data["chainTvls"].items():
    if isinstance(value, dict) and "tvl" in value:
        tvl_list = value["tvl"]
        if isinstance(tvl_list, list) and tvl_list:
            df = pd.DataFrame(tvl_list)
            chain_dfs[chain] = df
            print(f"\nDataFrame for {chain}")
            print(df.head())
        else:
            print(f"No TVL found for {chain}")
    else:
        print(f"\nUnexpected format for {chain}")

print(chain_dfs)
