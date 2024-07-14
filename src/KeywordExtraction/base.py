from abc import ABC, abstractmethod
from typing import List, Tuple

class KeywordExtractorInterface(ABC):
    @abstractmethod
    def extract(self, text: str) -> List[Tuple[str, float]]:
        pass