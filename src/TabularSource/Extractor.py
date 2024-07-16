from src.TabularSource.base import TabularSourceExtractorInterface

class Extractor:
    def __init__(self, client: TabularSourceExtractorInterface):
        self.db_client = client

    def extract(self, query: str)->list[dict]:
        return self.db_client.execute_query(query)
    
    def execute_query(self, query:str):
        return self.db_client.execute_query(query)
