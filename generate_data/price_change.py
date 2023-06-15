import pandas as pd
import random
import sqlite3

"""
Prompt:

Generate a python dataframe and data with the following column descriptions:

1. ETH price randomized over 30 days, highest value = 2500, lowest value = 800.
2. Percentage change: day-to-day percentage change, include percentage change between highest and lowest values.

Then repeat the above for BTC, but combine them in the same dataframe.
"""

# Set the random seed for reproducibility
random.seed(42)

# Define the number of days
num_days = 90

# Generate random data for ETH
eth_price = [random.uniform(800, 2500) for _ in range(num_days)]
eth_percentage_change = [((price - eth_price[0]) / eth_price[0]) * 100 for price in eth_price]

# Generate random data for BTC
btc_price = [random.uniform(30000, 60000) for _ in range(num_days)]
btc_percentage_change = [((price - btc_price[0]) / btc_price[0]) * 100 for price in btc_price]

# Create the DataFrame
data = {
    'ETH Price': eth_price,
    'ETH Percentage Change': eth_percentage_change,
    'BTC Price': btc_price,
    'BTC Percentage Change': btc_percentage_change
}
df = pd.DataFrame(data)

# Round the values to 2 decimal places
df = df.round(2)

# connect to the SQLite database
conn = sqlite3.connect('demo.db')

# push df to table in database
df.to_sql(name='price_change', con=conn, if_exists='replace', index=False)

# close db connection
conn.close()

print("---- data from price_changed pushed successfully ----.")