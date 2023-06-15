import pandas as pd
import random
import sqlite3

"""
Prompt
Generate a python dataframe and data with the following column descriptions:

1. ETH Buyers: Total number of buyers randomized over 90 days, highest value = 2 million, lowest value = 500K
2. ETH Purchased: Total amount of ETH purchased, ranging from 0 - 2.8K
3. ETH Total Supply: Total supply of ETH, day to day, ranging from 100 million to 120 million
4. ETH Price: Price of ETH, day to day, ranging from 800 to 2500
5. ETH Sellers: Total number of sellers randomized over 90 days, highest value = 1 million, lowest value = 200K
6. ETH Sold: Total amount of ETH sold, ranging from 0 - 1.5K

Then repeat the above for BTC, but combine them in the same dataframe.
"""

# Set the random seed for reproducibility
random.seed(42)

# Define the number of days
num_days = 90

# Generate random data for ETH
eth_buyers = [random.randint(500000, 2000000) for _ in range(num_days)]
eth_purchased = [random.uniform(0, 2800) for _ in range(num_days)]
eth_total_supply = [random.randint(100000000, 120000000) for _ in range(num_days)]
eth_price = [random.uniform(800, 2500) for _ in range(num_days)]
eth_sellers = [random.randint(200000, 1000000) for _ in range(num_days)]
eth_sold = [random.uniform(0, 1500) for _ in range(num_days)]

# Generate random data for BTC
btc_buyers = [random.randint(500000, 2000000) for _ in range(num_days)]
btc_purchased = [random.uniform(0, 2800) for _ in range(num_days)]
btc_total_supply = [random.randint(100000000, 120000000) for _ in range(num_days)]
btc_price = [random.uniform(800, 2500) for _ in range(num_days)]
btc_sellers = [random.randint(200000, 1000000) for _ in range(num_days)]
btc_sold = [random.uniform(0, 1500) for _ in range(num_days)]

# Create the DataFrame
data = {
    'ETH Buyers': eth_buyers,
    'ETH Purchased': eth_purchased,
    'ETH Total Supply': eth_total_supply,
    'ETH Price': eth_price,
    'ETH Sellers': eth_sellers,
    'ETH Sold': eth_sold,
    'BTC Buyers': btc_buyers,
    'BTC Purchased': btc_purchased,
    'BTC Total Supply': btc_total_supply,
    'BTC Price': btc_price,
    'BTC Sellers': btc_sellers,
    'BTC Sold': btc_sold
}
df = pd.DataFrame(data)

# Round the values to 2 decimal places
df = df.round(2)

# connect to the SQLite database
conn = sqlite3.connect('demo.db')

# push df to table in database
df.to_sql(name='volume', con=conn, if_exists='replace', index=False)

# close db connection
conn.close()

print("---- data from volume pushed successfully ----.")