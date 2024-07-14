from pymongo import MongoClient
from pymongo.collection import Collection

class MongoDBClient:
    def __init__(self, uri: str, database_name: str):
        self.client = MongoClient(uri)
        self.database = self.client[database_name]
        self.collections = self.database.list_collection_names()

    def get_collection(self, collection_name: str) -> Collection:
        return self.database[collection_name]

    def insert_documents(self, collection_name: str, documents: list):
        collection = self.get_collection(collection_name)
        result = collection.insert_many(documents)
        return result.inserted_ids
