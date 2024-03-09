import requests

# URL for the GET request
url = "https://stablecoins.llama.fi/stablecoin/5"

# Making the GET request
response = requests.get(url)

# Checking the response status and printing the result
if response.status_code == 200:
    # Response is successful
    print("Success! Here's the response data:", response.json())
else:
    # Response failed
    print(f"Failed to retrieve data. Status code: {response.status_code}")
