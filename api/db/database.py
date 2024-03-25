from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

db_host = os.getenv("MONGO_DB_URL")
db = os.getenv("MONGO_DB")

CONNECTION_STRING = db_host
client = MongoClient(CONNECTION_STRING)
database = client[db]