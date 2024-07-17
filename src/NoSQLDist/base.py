from abc import ABC, abstractmethod

class NoSQLInterface(ABC):
    @abstractmethod
    def load_increment(data:dict, collection:str, source_PK=str, dist_PK=str):
        pass
    
    @abstractmethod
    def update(self, collection_name:str, filter_query:dict[str:any], value:dict[str:any]):
        pass
    
    @abstractmethod
    def find(self, collection_name: str, filter_query: dict, cols_to_show: dict = {}):
        pass
    
    @abstractmethod
    def create_view(self, view_name:str, view_on:str, pipeline: list=[]):
        pass
    
    @abstractmethod
    def drop_view(self, view_name:str):
        pass