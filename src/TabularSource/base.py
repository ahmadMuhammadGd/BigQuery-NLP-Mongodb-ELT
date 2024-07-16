from abc import ABC, abstractmethod

class TabularSourceExtractorInterface(ABC):
    @abstractmethod
    def execute_query(self, query: str):
        pass
    