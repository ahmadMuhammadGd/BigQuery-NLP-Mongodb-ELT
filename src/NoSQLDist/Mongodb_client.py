from pymongo import MongoClient, UpdateOne
from pymongo.collection import Collection
from src.NoSQLDist.base import NoSQLInterface

class MongoDBClient(NoSQLInterface):
    def __init__(self, uri: str, database_name: str):
        self.client = MongoClient(uri)
        self.database = self._get_database(database_name)
        self.collections = self.database.list_collection_names()

    def _get_database(self, database_name):
        return self.client[database_name]
    
    def _get_collection(self, collection_name: str) -> Collection:
        return self.database[collection_name]

    def insert_documents(self, collection_name: str, documents: list):
        collection = self._get_collection(collection_name)
        collection.insert_many(documents)

    def load_increment(self, data: list[dict], collection_name: str, source_PK=..., dist_PK=...):
        collection = self._get_collection(collection_name)
        bulk_operations = []
        for entry in data:
            filter_query = {dist_PK: entry[source_PK]}
            update_doc = {"$set": entry}
            bulk_operations.append(UpdateOne(filter_query, update_doc, upsert=True))
        if bulk_operations:
            collection.bulk_write(bulk_operations)

    def create_index(self, collection_name: str, key_name: str, unique: bool = False):
        collection = self._get_collection(collection_name)
        collection.create_index(key_name, unique=unique)
        
    def update(self, collection_name: str, filter_query: dict, value: dict):
        collection = self._get_collection(collection_name)
        collection.update_one(filter_query, {"$set": value})

    def find(self, collection_name: str, filter_query: dict, cols_to_show: dict = {}):
        collection = self._get_collection(collection_name)
        return collection.find(filter_query, cols_to_show)

