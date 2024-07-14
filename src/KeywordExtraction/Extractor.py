from typing import List, Tuple
from src.KeywordExtraction.Extractor import KeywordExtractorInterface

class KeywordExtractor:
    def __init__(self, extractor: KeywordExtractorInterface):
        self.extractor = extractor

    def extract(self, text: str) -> List[Tuple[str, float]]:
        return self.extractor.extract(text)
