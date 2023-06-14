import pandas as pd
import random

"""
Prompt:

Generate a python dataframe and data with the following column descriptions:

1. ETH price randomized over 30 days, highest value = 2500, lowest value = 800.
2. Percentage change: day-to-day percentage change, include percentage change between highest and lowest values.
"""

# Set the random seed for reproducibility
random.seed(42)

# Define the number of days
num_days = 30

# Generate random ETH prices between 800 and 2500
eth_prices = [random.uniform(800, 2500) for _ in range(num_days)]

# Calculate the day-to-day percentage change
percentage_change = [(eth_prices[i] - eth_prices[i-1]) / eth_prices[i-1] * 100 for i in range(1, num_days)]
percentage_change.insert(0, (eth_prices[0] - eth_prices[num_days-1]) / eth_prices[num_days-1] * 100)

# Create the DataFrame
data = {'ETH Price': eth_prices, 'Percentage Change': percentage_change}
df = pd.DataFrame(data)

# Round the values to 2 decimal places
df = df.round(2)

print(df)