import pandas as pd
import random
import sqlite3

"""
Prompt
Generate a python dataframe and data with the following column descriptions:

1. ETH Price randomized over 90 days, highest value = 2500, lowest value = 800.
2. Total Supply: Total supply of ETH, day to day, ranging from 100 million to 120 million.
3. Market Cap: ETH Price (column 1) multiplied by Total Supply (column 2)

"""

# Set the random seed for reproducibility
random.seed(42)

# Define the number of days
num_days = 90

# Generate random data for each column
eth_price = [random.uniform(800, 2500) for _ in range(num_days)]
total_supply = [random.randint(100000000, 120000000) for _ in range(num_days)]
market_cap = [eth_price[i] * total_supply[i] for i in range(num_days)]

# Create the DataFrame
data = {
    'ETH Price': eth_price,
    'Total Supply': total_supply,
    'Market Cap': market_cap
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