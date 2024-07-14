import yake
from typing import List, Tuple
from src.KeywordExtraction.base import KeywordExtractorInterface

class YakeKeywordExtractor(KeywordExtractorInterface):
    def __init__(self):
        self.kw_extractor = self._extractor_init()

    def _extractor_init(self) -> yake.KeywordExtractor:
        return yake.KeywordExtractor()

    def extract(self, text: str) -> List[Tuple[str, float]]:
        return self.kw_extractor.extract_keywords(text)
