from src.NoSQLDist.base import NoSQLInterface

class Loader:
    def __init__(self, db_client: NoSQLInterface):
        self.db_client = db_client
        
    def load_incremental(self, collection_name:str, data:list[dict], source_PK:str, dist_PK:str):
        self.db_client.load_increment(
            data=data,
            collection_name=collection_name,
            source_PK=source_PK,
            dist_PK=dist_PK
        )
    def update(self, collection_name:str, filter_query:dict[str:any], value:dict[str:any]):
        self.db_client.update(
            collection_name = collection_name,
            filter_query = filter_query,
            value=value
        )
    def find(self, collection_name: str, filter_query: dict, cols_to_show: dict = {}):
        return self.db_client.find(
            collection_name=collection_name,
            filter_query=filter_query,
            cols_to_show=cols_to_show
        )
