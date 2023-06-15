import pandas as pd
import random

"""
Prompt
Generate a python dataframe and data with the following column descriptions:

1. Buyers: Total number of buyers randomized over 90 days, highest value = 2 million, lowest value = 500K
2. Purchased: Total amount of ETH purchased, ranging from 0 - 2.8K
3. Total Supply: Total supply of ETH, day to day, ranging from 100 million to 120 million
4. Price: Price of ETH, day to day, ranging from 800 to 2500
5. Sellers: Total number of sellers randomized over 90 days, highest value = 1 million, lowest value = 200K
6. Sold: Total amount of ETH sold, ranging from 0 - 1.5K
"""

# Set the random seed for reproducibility
random.seed(42)

# Define the number of days
num_days = 90

# Generate random data for each column
buyers = [random.randint(500000, 2000000) for _ in range(num_days)]
purchased = [random.uniform(0, 2800) for _ in range(num_days)]
total_supply = [random.randint(100000000, 120000000) for _ in range(num_days)]
price = [random.uniform(800, 2500) for _ in range(num_days)]
sellers = [random.randint(200000, 1000000) for _ in range(num_days)]
sold = [random.uniform(0, 1500) for _ in range(num_days)]

# Create the DataFrame
data = {
    'Buyers': buyers,
    'Purchased': purchased,
    'Total Supply': total_supply,
    'Price': price,
    'Sellers': sellers,
    'Sold': sold
}
df = pd.DataFrame(data)

# Round the values to 2 decimal places
df = df.round(2)

print(df)