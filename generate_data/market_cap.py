import pandas as pd
import random
import sqlite3

"""
Prompt
Generate a python dataframe and data with the following column descriptions:

1. ETH Price randomized over 90 days, highest value = 2500, lowest value = 800.
2. Total Supply: Total supply of ETH, day to day, ranging from 100 million to 120 million.
3. Market Cap: ETH Price (column 1) multiplied by Total Supply (column 2)

Then repeat the above for BTC, but combine them in the same dataframe.
"""

# Set the random seed for reproducibility
random.seed(42)

# Define the number of days
num_days = 90

# Generate random data for ETH
eth_price = [random.uniform(800, 2500) for _ in range(num_days)]
eth_total_supply = [random.uniform(100e6, 120e6) for _ in range(num_days)]
eth_market_cap = [price * supply for price, supply in zip(eth_price, eth_total_supply)]

# Generate random data for BTC
btc_price = [random.uniform(800, 2500) for _ in range(num_days)]
btc_total_supply = [random.uniform(15e6, 20e6) for _ in range(num_days)]
btc_market_cap = [price * supply for price, supply in zip(btc_price, btc_total_supply)]

# Create the DataFrame
data = {
    'ETH Price': eth_price,
    'ETH Total Supply': eth_total_supply,
    'ETH Market Cap': eth_market_cap,
    'BTC Price': btc_price,
    'BTC Total Supply': btc_total_supply,
    'BTC Market Cap': btc_market_cap
}
df = pd.DataFrame(data)

# Round the values to 2 decimal places
df = df.round(2)

# connect to the SQLite database
conn = sqlite3.connect('demo.db')

# push df to table in database
df.to_sql(name='market_cap', con=conn, if_exists='replace', index=False)

# close db connection
conn.close()

print("---- data from market_cap pushed successfully ----.")