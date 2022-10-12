import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import text 

import requests
import json
import pandas as pd 
from pprint import pprint 

import os
# using python-dotenv method
from dotenv import load_dotenv
load_dotenv()

db_user = os.environ.get('DB_USER')
db_password = os.environ.get('DB_PASSWORD')

# database connection string
db_string = f'postgresql://{db_user}:{db_password}@localhost:5432/credmark'
db = create_engine(db_string)

# create test table
# db.execute("CREATE TABLE IF NOT EXISTS films (title TEXT, director TEXT, year TEXT)")

# insert data
db.execute("INSERT INTO films (title, director, year) VALUES ('Thor: Love & Thunder', 'Taika Waititi', '2022')")

# read data
result_set = db.execute("SELECT * FROM films")

for r in result_set:
    print(r)