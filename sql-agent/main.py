import os
from dotenv import load_dotenv
load_dotenv()
api_key=os.getenv('OPENAI_API_KEY')
print(api_key)


from langchain_community.utilities import SQLDatabase

db = SQLDatabase.from_uri("sqlite:///Chinook.db")
print(db.dialect)
print(db.get_usable_table_names())
db.run("SELECT * FROM Artist LIMIT 10;")