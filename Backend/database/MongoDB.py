from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path='.env')

class MongoDB(object):
    def __init__(self) -> None:
        self._CONNECTION_STRING=os.getenv(key='CONNECTION_STRING')
        
    def connectDB(self, collectionName:str):
        client=MongoClient(self._CONNECTION_STRING)
        collection=client[collectionName]
        return  client, collection

        