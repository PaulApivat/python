import requests
import os
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

url = "https://api.coingecko.com/api/v3/coins/renzo-restaked-eth/ohlc?vs_currency=usd&days=180&precision=18"

headers = {
    "accept": "application/json",
    "x-cg-demo-api-key": os.getenv("COINGECKO_API"),
}

response = requests.get(url, headers=headers)

##print(response.text)

data = response.json()

# Create DataFrame with appropriate column names
df = pd.DataFrame(data, columns=["timestamp", "open", "high", "low", "close"])

# Convert timestamp (milliseconds) to datetime
df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")

print(df)
