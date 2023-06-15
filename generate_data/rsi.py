import pandas as pd
import random
import sqlite3

"""
Prompt
Generate a python dataframe and data with the following column descriptions:

1. ETH Purchased: Total amount of ETH purchased, ranging from 0 - 2.8K, randomized over 90 days.
2. ETH Sold: Total amount of ETH sold, ranging from 0 - 1.5K
3. ETH Price: Price of ETH, day to day, ranging from 800 to 2500
4. ETH Percentage Price Change: day-to-day percentage change in price
5. ETH Relative Strength (RS): Divide average positive price changes by average of negative price changes.
6. ETH Relative Strength Index: 100 - 100/(1 + RS) for each day

Then repeat the above for BTC, but combine them in the same dataframe.
"""

# Set the random seed for reproducibility
random.seed(42)

# Define the number of days
num_days = 90

# Generate random data for ETH
eth_purchased = [random.uniform(0, 2800) for _ in range(num_days)]
eth_sold = [random.uniform(0, 1500) for _ in range(num_days)]
eth_price = [random.uniform(800, 2500) for _ in range(num_days)]
eth_percentage_change = [(eth_price[i] - eth_price[i-1]) / eth_price[i-1] * 100 if i > 0 else 0 for i in range(num_days)]
eth_positive_changes = [change for change in eth_percentage_change if change > 0]
eth_negative_changes = [change for change in eth_percentage_change if change < 0]
eth_rs = sum(eth_positive_changes) / abs(sum(eth_negative_changes)) if eth_negative_changes else 0
eth_rsi = 100 - 100 / (1 + eth_rs)

# Generate random data for BTC
btc_purchased = [random.uniform(0, 2800) for _ in range(num_days)]
btc_sold = [random.uniform(0, 1500) for _ in range(num_days)]
btc_price = [random.uniform(800, 2500) for _ in range(num_days)]
btc_percentage_change = [(btc_price[i] - btc_price[i-1]) / btc_price[i-1] * 100 if i > 0 else 0 for i in range(num_days)]
btc_positive_changes = [change for change in btc_percentage_change if change > 0]
btc_negative_changes = [change for change in btc_percentage_change if change < 0]
btc_rs = sum(btc_positive_changes) / abs(sum(btc_negative_changes)) if btc_negative_changes else 0
btc_rsi = 100 - 100 / (1 + btc_rs)

# Create the DataFrame
data = {
    'ETH Purchased': eth_purchased,
    'ETH Sold': eth_sold,
    'ETH Price': eth_price,
    'ETH Percentage Price Change': eth_percentage_change,
    'ETH Relative Strength (RS)': eth_rs,
    'ETH Relative Strength Index (RSI)': eth_rsi,
    'BTC Purchased': btc_purchased,
    'BTC Sold': btc_sold,
    'BTC Price': btc_price,
    'BTC Percentage Price Change': btc_percentage_change,
    'BTC Relative Strength (RS)': btc_rs,
    'BTC Relative Strength Index (RSI)': btc_rsi
}
df = pd.DataFrame(data)

# Round the values to 2 decimal places
df = df.round(2)

# connect to the SQLite database
conn = sqlite3.connect('demo.db')

# push df to table in database
df.to_sql(name='rsi', con=conn, if_exists='replace', index=False)

# close db connection
conn.close()

print("---- data from rsi pushed successfully ----.")