from MongoDB import MongoDB

class User(object):
    def __init__(self) -> None:
        self.mongoDB=MongoDB()
    
    def addUser(self, data:dict):
        try:
            client, database, collection=self.mongoDB.connectDB(databaseName='Test', collectionName='User')
            collection.insert_one(data)
        finally:
            client.close()
        
