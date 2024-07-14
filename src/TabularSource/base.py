from abc import ABC, abstractmethod

class TabularSourceExtractorInterface(ABC):
    @abstractmethod
    def extract(self, query: str):
        pass