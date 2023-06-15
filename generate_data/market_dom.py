import pandas as pd
import random

"""
Prompt
Generate a python dataframe and data with the following column descriptions:

1. BTC: Market capitalization downward trend over 90 days, lowest value = $300 Billion, highest value = $589 Billion
2. ETH: Market capitalization downward trend over 90 days, lowest value = $198 Billion, highest value = $254 Billion
3. BNB: Market capitalization downward trend over 90 days, lowest value = $967 Million, highest value = $54 Billion
4. USDC: Market capitalization downward trend over 90 days, lowest value = $3.2 Billion, highest value = $37 Billion
5. LIDO stETH: Market capitalization downward trend over 90 days, lowest value = $9.8 Billion, highest value = $13.4 Billion
6. SOL: Market capitalization downward trend over 90 days, lowest value = $5.8 Billion, highest value = $10 Billion
7. POLYGON: Market capitalization downward trend over 90 days, lowest value = $5.1 Billion, highest value = $11.3 Billion
8. AVAX: Market capitalization downward trend over 90 days, lowest value = $3.9 Billion, highest value = $6.9 Billion
9. UNISWAP: Market capitalization downward trend over 90 days, lowest value = $2.9 Billion, highest value = $4.9 Billion
10. LINK: Market capitalization downward trend over 90 days, lowest value = $2.6 Billion, highest value = $4.4 Billion

"""

# Set the random seed for reproducibility
random.seed(42)

# Define the number of days
num_days = 90

# Generate random data for each column
btc = [random.uniform(300, 589) for _ in range(num_days)]
eth = [random.uniform(198, 254) for _ in range(num_days)]
bnb = [random.uniform(967, 54000) for _ in range(num_days)]
usdc = [random.uniform(3.2, 37) for _ in range(num_days)]
lido_steth = [random.uniform(9.8, 13.4) for _ in range(num_days)]
sol = [random.uniform(5.8, 10) for _ in range(num_days)]
polygon = [random.uniform(5.1, 11.3) for _ in range(num_days)]
avax = [random.uniform(3.9, 6.9) for _ in range(num_days)]
uniswap = [random.uniform(2.9, 4.9) for _ in range(num_days)]
link = [random.uniform(2.6, 4.4) for _ in range(num_days)]

# Create the DataFrame
data = {
    'BTC': btc,
    'ETH': eth,
    'BNB': bnb,
    'USDC': usdc,
    'LIDO stETH': lido_steth,
    'SOL': sol,
    'POLYGON': polygon,
    'AVAX': avax,
    'UNISWAP': uniswap,
    'LINK': link
}
df = pd.DataFrame(data)

# Round the values to 2 decimal places
df = df.round(2)

print(df)