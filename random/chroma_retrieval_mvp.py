import openai 
import chromadb   
import os
import re

from collections.abc import Iterable, Container
from pprint import pprint

# use python-dotenv to get API key
from dotenv import load_dotenv
load_dotenv()



# Helper functions
def replace_ticker(queries, ticker: str) -> list:
    return [query.replace('{ticker}', ticker) for query in queries]


# User queries - batch single queries into a list; split across 2 assets - ETH & BTC
assets = ["ETH", "BTC"]

# Q1-3: Price Changes
# Q4-5: Volume
# Q6: RSI
# Q7-9: Market Cap
# Q10: Market Dominance
# Q11-13: News
user_queries = [
    "What are the biggest price changes of {ticker} in the last 30 days?", 
    "How quickly has {ticker} price moved over the past 30 days?",
    "How volatile is {ticker} trading in the past month?",

    "What is the level of {ticker} buying over the past 30 days?",
    "What is the level of {ticker} selling over the past 30 days",

    "How does the level of {ticker} buying compare to the level of {ticker} selling for the past month?",
  
    "What is the current total dollar market value of {ticker}?",
    "Has {ticker} reached its all-time high recently?",
    "How close is {ticker} to its ATL?",

    "How does the current total dollar market value of {ticker} compare to other projects?",

    "Are there any upcoming major vesting events for {ticker}?",
    "Are there any updates from the core developers for {ticker}?",
    "Are the market participants bullish or bearish for {ticker}?"
]

# user helper function to create two lists of queries for each ETH & BTC
all_queries_assets = [ replace_ticker(user_queries, asset) for asset in assets ]

#pprint(all_queries_assets)

# Take two list of queries for ETH & BTC
# run the openai.Completion.create() function over each of them
# need to insert an initial prompt to OpenAI
# This prompt Expands the initial one-line questions into a more comprehensive interpretation of user intent

def prompt(query: str) -> str:
    return f"""
    Role: You are a language model metric dispatcher for a crypto analyst. Your task is to interpret and expand user queries related to cryptocurrency quantitative metrics. 
    The expanded form should provide a more comprehensive interpretation of the user's intent and the type of data that would best address their question.
    Instruction: Taker the user's query, interpret its underlying intention, and expand it to include more detail and context. Your expansion should indicate what kind of data, metrics, or insights would best addres the user's query. 
    Remember to keep the language clear, descriptive, and related to the user's original question. Provide the ticker, description of the metric, your current user case, and how it gets used.
    Type of metrics you have access to are: Techical Analysis indicators, price metrics, token distribution, company token vesting, official social announcement channels, thread discussion on twitter.

    Example:

    Input:
    User query:
    "What is the current price of $ETH?"

    Output:
    Metric("$ETH", "The user is interested in the current market price of the $ETH token. They're likely trying to get a quick understanding of its present valuation. The metric should simply present the most up-to-date market price for $ETH today")

    Input:
    User query:
    "{query}"

    Output:
    """

openai.api_key = os.environ.get("OPENAI_API_KEY")

def open_ai_prompt(prompt: str, temp=0.3) -> str:
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=2047,
        temperature=temp
    )
    return response.choices[0].text.strip()


user_and_llm_queries = []

for queries in all_queries_assets:
    expanded_queries = [ open_ai_prompt(prompt(q)) for q in queries]
    #print(expanded_queries)
    for index, eq in enumerate(expanded_queries):
        user_and_llm_queries.append({"query": queries[index], "expansion": eq})

pprint(user_and_llm_queries)

# Revised Questions to reflect MVP Engineering Spec
# Price Changes, RSI, ETH, Volume, Marketcap, Market Dominance, News
# create helper functions to turn Openai-Expanded questions (intention)
# into individual tools


# price change includes magnitude, speed and volatility of price changes. 
# note: combining 3 metrics into 1 implies 3 user queries should be matched to this one function
def price_change(ticker: str) -> str:
    return f"""Name: {ticker} Price Change ({ticker}PC)

    Description: The ticker Price Change, or {ticker}PC, measures the biggest price changes of the ${ticker} token over the past 30 days including highest and lowest values. 
    This metric should provide insight into range of price movements for ${ticker} over the past 30 days; this could be percentage change between highest and lowest values.
    Finally, this indicator shows how fast prices of {ticker} has changed over the past 30 days; this could be measured as percentage change over that time period. 

    When to use: Use {ticker}PC to get a better understanding of the biggest price changes of {ticker} in the past 30 days.
    {ticker}PC may also indicate how quickly {ticker} price has moved. 
    Finally, this data can be used to understand the risk associated with investing in ${ticker}.
    """

def volume(ticker: str) -> str:
    return f"""
    """


def rsi(ticker: str) -> str:
    return f"""
    """

def market_cap(ticker: str) -> str:
    return f"""
    """

def market_dom(ticker: str) -> str:
    return f"""
    """

def news(ticker: str) -> str:
    return f"""
    """

