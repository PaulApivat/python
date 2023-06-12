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

user_queries = [
    "How has {ticker} performed over the last week?",
    "How volatile is {ticker} trading in the past month?",
    "Has {ticker} reached its all-time high recently?",
    "What percentage of {ticker}'s total supply is already in circulation?",
    "How close is {ticker} to its ATL?",
    "Are there any upcoming major vesting events for {ticker}?",
    "Are there any updates from the core developers for {ticker}?",
    "Are the market participants bullish or bearish for {ticker}?",
    "What's the price trend of {ticker} for the past 30 days?",
    "What are the biggest price changes of {ticker} in the last 7 days?"
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