import json
import random
from pprint import pprint

"""
Prompt

Generate 90 news headlines about the following crypto assets: BTC, ETH, USDC, UNISWAP, LINK. Make each headline 1-2 sentences long. The headlines can be about the following topics: major vesting events, project updates, announcements, and discussions surrounding the token from core developers and official team sources. Headlines can include discussions about exchange listings, collaborations, partnerships, to major events and milestones and product updates.

The 90 headlines will be stored in python dictionaries inside a JSON with the following keys:
- id
- news headline
- topic
- asset

"""

# Set the random seed for reproducibility
random.seed(42)

# Define the crypto assets and topics
crypto_assets = ['BTC', 'ETH', 'USDC', 'UNISWAP', 'LINK']
topics = ['Major Vesting Events', 'Project Updates', 'Announcements', 'Discussions']

# Generate news headlines for each day
num_days = 90
data = []
for i in range(num_days):
    headline_id = i + 1
    asset = random.choice(crypto_assets)
    topic = random.choice(topics)
    
    headline = ''
    if topic == 'Major Vesting Events':
        headline = f"{asset} announces major vesting event for token holders."
    elif topic == 'Project Updates':
        headline = f"{asset} releases important project updates and improvements."
    elif topic == 'Announcements':
        headline = f"{asset} makes exciting announcements about upcoming developments."
    elif topic == 'Discussions':
        headline = f"{asset} core developers engage in discussions about the future of the protocol."
    
    news_dict = {
        'id': headline_id,
        'news headline': headline,
        'topic': topic,
        'asset': asset
    }
    data.append(news_dict)

# Convert the data to JSON format
json_data = json.dumps(data, indent=4)

pprint(data)