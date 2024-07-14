from Mongodb_client import MongoDBClient

class Loader:
    def __init__(self, mongodb_client: MongoDBClient):
        self.mongodb_client = mongodb_client

    def load(self, collection_name: str, data: list):
        self.mongodb_client.insert_documents(collection_name, data)
