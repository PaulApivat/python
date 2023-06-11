import openai 
import chromadb
import os

from collections.abc import Iterable, Container

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

def price_snapshot(ticker: str) -> str:
    return f"""
    Name: {ticker} Price Trend Indicator ({ticker}PTI)
    Description: The {ticker} Price Trend Indicator, or {ticker}PTI, provides a simple but comprehensive snapshot of the {ticker} token's price performance. It includes the current price which indicates its present value, and the price in the last 7 days, 30 days, 90 days and 180 days and include the percentage changes from the All-Time High (ATH) and all-time low (ATL).
    When to use: Use {ticker}PTI when you want a quick overview of the {ticker} token's recent price history and its position relative to its ATH and ATL. This can give you a glance of the token's price trend and volatility, helping to inform your investment decisions.   
    """

def volume(ticker: str) -> str:
    return f"""
    Name: Major Exchange Trading Volume Metrics
    Description: This metric includes both the aggregate and average trading volumes for the {ticker} token on major cryptocurrency exchanges. The data incorporates daily trading volumes, offering a comprehensive view of the token's liquidity and market activity across these key platforms.
    When to use: Use this metric when you want to evaluate the token's liquidity, trading activity, and market presence across major exchanges. It's particularly useful for understanding the distribution of trading volume and identifying which exchanges are driving the most activity for {ticker}.
    """

def token_dis(ticker: str) -> str:
    return f"""
    Name: {ticker} Token Distribution Ratio ({ticker}TDR)
    Description: The {ticker} Token Distribution Ratio, or {ticker}TDR, measures the proportion of the token's circulating supply compared to its total supply. This is calculated by dividing the circulating supply by the total supply. The result, expressed as a percentage, provides a snapshot of the token's distribution status and the potential inflationary impact of future token releases.
    When to use: Use {ticker}TDR when you want to understand the potential inflationary risk associated with a token. A higher ratio indicates a larger proportion of the total supply is already in circulation, which might suggest a lower risk of inflation due to future token releases.
    """

def vesting_sched(ticker: str) -> str:
    return f"""
    Name: {ticker} Vesting Schedule Overview ({ticker}VSD)
    Description: The {ticker} Vesting Schedule Overview, or {ticker}VSO, provides information on the vesting schedule of the token's allocated supply. This includes the total number of tokens to be released, the release schedule (how many tokens are released per time unit), and the duration of the vesting period.
    When to use: Use {ticker}VSO when you want to assess the future supply impact of tokens being released according to a vesting schedule. This can help inform your understanding of potential future selling pressure from insiders.
    """

def twitter_news(ticker: str) -> str:
    return f"""
    Name: Recent Twitter News and Events for {ticker}
    Description: This metric gathers and analyzes recent tweets and Twitter threads related to the {ticker} token. It includes key information about news, updates, announcements, and discussions surrounding the token from teams and official sources. This can include everything from exchange listings, collaborations, partnerships, to major events and milestones and product updates
    When to use: Use this metric when you want to stay updated with the latest news and events related to {ticker}, or when assessing the impact of social media, in particular Crypto Twitter threads  activity on the token. The sources are coming from core developer team, founder and official comms.
    """

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

def open_ai_prompt(prompt: str, temp=0.3) -> str:
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=2047,
        temperature=temp
    )
    return response.choices[0].text.strip()

def replace_ticker(queries, ticker: str) -> list:
    return [query.replace('{ticker}', ticker) for query in queries]


def parse_metric_output(output: str) -> tuple:
    # Match all characters (string) between quotes in the output
    matches = re.findall(r'"([^"]*)"', output)

    if len(matches) == 2:
        return tuple(matches)
    else:
        return None

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

all_queries_assets = [ replace_ticker(user_queries, asset) for asset in assets ]
# print(all_queries_assets)

user_and_llm_queries = []

for queries in all_queries_assets:
    expanded_queries = [ open_ai_prompt(prompt(q)) for q in queries]
    print(expanded_queries)
    for index, eq in enumerate(expanded_queries):
        user_and_llm_queries.append({"query": queries[index], "expansion": eq})
print(user_and_llm_queries)

# ChromaDB add collection
for i, ticker in enumerate(assets):
    collection.add(
        documents=[vol(ticker), macd(ticker), rsi(ticker), price_snapshot(ticker), token_dis(ticker), vesting_sched(ticker), twitter_news(ticker)],
        metadatas=[{"asset": ticker}, {"asset": ticker}, {"asset": ticker}, {"asset": ticker}, {"asset": ticker}, {"asset": ticker}, {"asset": ticker}],
        ids=[ ticker+str(ind) for ind in range(1,8)]
    )

outputs = []

for q in user_and_llm_queries:
    results = collection.query(
        query_texts=[q["query"], q["expansion"]],
        n_results=1,
    )
    print('\n')
    print('user query: ', q["query"])
    print('expansion query: ', q["expansion"])
    print('ids:', results["ids"])
    print('documents:', results["documents"])
    print('documents:', results["distances"])
    outputs.append({"user_query": q["query"],
                    "expansion_query": q["expansion"],
                    "ids": results["ids"],
                    "documents": results["documents"],
                    "distances": results["distances"]
                    })

# placeholder