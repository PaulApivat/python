import sqlalchemy 
from sqlalchemy import create_engine 
from sqlalchemy import text
import os 

# using python-dotenv
from dotenv import load_dotenv
load_dotenv()

# reference python-dotenv 

db_user = os.environ.get('DB_USER')
db_password = os.environ.get('DB_PASSWORD')

db_string = f'postgresql://{db_user}:{db_password}@35.198.200.35:5432/postgres'
db = create_engine(db_string)
conn = db.connect()

print(db)
print(conn)

# get output column from stableprice3 table in postgres
def get_output():
    with db.connect() as conn:
        query = "SELECT * FROM stableprice3;"
        result = conn.execute(text(query))
        for row in result:
            print(row)


if __name__ == '__main__':
    get_output()
