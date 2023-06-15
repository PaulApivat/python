import pandas as pd
import random

"""
Prompt
Generate a python dataframe and data with the following column descriptions:

1. Purchased: Total amount of ETH purchased, ranging from 0 - 2.8K, randomized over 90 days.
2. Sold: Total amount of ETH sold, ranging from 0 - 1.5K
3. Price: Price of ETH, day to day, ranging from 800 to 2500
4. Percentage Price Change: day-to-day percentage change in price
5. Relative Strength (RS): Divide average positive price changes by average of negative price changes.
6. Relative Strength Index: 100 - 100/(1 + RS) for each day
"""

# Set the random seed for reproducibility
random.seed(42)

# Define the number of days
num_days = 90

# Generate random data for each column
purchased = [random.uniform(0, 2800) for _ in range(num_days)]
sold = [random.uniform(0, 1500) for _ in range(num_days)]
price = [random.uniform(800, 2500) for _ in range(num_days)]
percentage_change = [(price[i] - price[i-1]) / price[i-1] * 100 for i in range(1, num_days)]
percentage_change.insert(0, 0)  # Insert 0 for the first day
average_positive_changes = sum([change for change in percentage_change if change > 0]) / num_days
average_negative_changes = sum([change for change in percentage_change if change < 0]) / num_days
rs = average_positive_changes / abs(average_negative_changes)
rsi = 100 - (100 / (1 + rs))

# Create the DataFrame
data = {
    'Purchased': purchased,
    'Sold': sold,
    'Price': price,
    'Percentage Price Change': percentage_change,
    'Relative Strength (RS)': rs,
    'Relative Strength Index (RSI)': rsi
}
df = pd.DataFrame(data)

# Round the values to 2 decimal places
df = df.round(2)

print(df)