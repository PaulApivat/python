import json
import pprint

# Statement 1: Bullish Nature
bullish_statement = {
    "name": "FXS",
    "description": "Frax Shares - Showing a bullish trend with increasing prices. The exponential moving average (EMA) is trending upwards, indicating positive price momentum. The 1-day price change is positive, and the 7-day price change is also positive, reflecting a strong bullish sentiment.",
    "behavior": "Bullish",
}

# Statement 2: Bearish Nature
bearish_statement = {
    "name": "FXS",
    "description": "Frax Shares - Exhibiting a bearish trend with decreasing prices. The exponential moving average (EMA) is trending downwards, suggesting negative price momentum. The 1-day price change is negative, and the 7-day price change is also negative, indicating a bearish sentiment in the market.",
    "behavior": "Bearish",
}

# Statement 3: Mixed Behavior
mixed_statement = {
    "name": "FXS",
    "description": "Frax Shares - Displaying a mixed behavior with no clear trend. The exponential moving average (EMA) is relatively flat, indicating a lack of strong momentum in either direction. The 1-day price change may be positive or negative, and the 7-day price change may also vary, suggesting uncertainty and a mixed sentiment among traders.",
    "behavior": "Mixed",
}

# Store dictionaries in a JSON data structure
data = {
    "bullish_statement": bullish_statement,
    "bearish_statement": bearish_statement,
    "mixed_statement": mixed_statement,
}

#json_data = json.dumps(data, indent=0)

json_data = json.dumps(data, indent=4)

#pprint.pprint(json_data)

pprint.pprint(json_data)