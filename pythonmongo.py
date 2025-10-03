from dotenv import load_dotenv
import os
import pymongo

load_dotenv()
MONGO_URL=os.getenv("MONGO_URL")
# pymongo.MongoClient("")
