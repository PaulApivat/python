import openai 
import chromadb
import os

chroma_client = chromadb.Client()
collection = chroma_client.create_collection(name="metrics")

# use python-dotenv to get API key
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.environ.get("OPENAI_API_KEY")

# helper functions that return strings

def vol(ticker: str) -> str:
    return f"""Name: {ticker} Volatility Index ({ticker}VI)
    Description: The ticker Volatility Index, or {ticker}VI, measures the market's expectation of 30-day forward-looking volatility, derived from real-time ${ticker} token price options. It is calculated by extrapolating implied volatilities on ${ticker} token prices to determine expected price fluctuations.
    When to use: Use {ticker}VI when you want to understand the market's expectation of the price volatility of the ${ticker} token. A higher {ticker}VI may indicate a higher potential for price swings, signifying greater risk and opportunity.
    """

def macd(ticker: str) -> str:
    return f"""Name: {ticker} Moving Average Convergence Divergence ({ticker}MACD)
    Description: The {ticker} Moving Average Convergence Divergence, or {ticker}MACD, is a trend-following momentum indicator that shows the relationship between two moving averages of the ${ticker} token's price. It is calculated by subtracting the 26-day Exponential Moving Average (EMA) from the 12-day EMA. A nine-day EMA of the {ticker}MACD, called the "signal line", is then plotted on top of the MACD, functioning as a trigger for buy and sell signals.
    When to use: Use {ticker}MACD when you want to identify potential buy and sell signals for the ${ticker} token. When the {ticker}MACD crosses above the signal line, it may be a good time to buy. Conversely, when it crosses below the signal line, it may be a good time to sell.
    """

def rsi(ticker: str) -> str:
    return f"""Name: {ticker} Relative Strength Index ({ticker}RSI)
    Description: The {ticker} Relative Strength Index, or {ticker}RSI, is a momentum indicator that measures the speed and change of price movements of the ${ticker} token. It oscillates between zero and 100 and is typically used with a 14-day timeframe. Traditionally, the ${ticker} token is considered overbought when the {ticker}RSI is above 70 and oversold when it's below 30.
    When to use: Use {ticker}RSI when you want to identify potentially overbought or oversold conditions for the ${ticker} token. This can help inform decisions about when to buy or sell the token.
    """

