import pandas as pd
from sqlalchemy import create_engine

# environment variables
import os
from dotenv import load_dotenv
load_dotenv()

string = os.environ.get('db_string')
engine = create_engine(string)

query = """
SELECT * 
FROM coordinape_rounds_3
LIMIT 10
"""

coordinape_calls = pd.read_sql(query, engine)

print(coordinape_calls)
