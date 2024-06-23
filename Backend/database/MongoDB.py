from pymongo import MongoClient
from dotenv import load_dotenv
import os
from threading import Lock

load_dotenv(dotenv_path='.env')

class MongoDB(object):
    def __init__(self) -> None:
        self._CONNECTION_STRING=os.getenv(key='CONNECTION_STRING')
        self._client=None
        self.lock=Lock()
        
    def connectDB(self, collectionName:str):
        if self._client is None:
            with self.lock:
                if self._client is None:
                    client=MongoClient(self._CONNECTION_STRING)
                    collection=client[collectionName]
                    
        return  client, collection

        