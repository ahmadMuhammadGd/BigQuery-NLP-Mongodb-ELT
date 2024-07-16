import yake
from typing import List, Tuple
from src.KeywordExtraction.base import KeywordExtractorInterface

class YakeKeywordExtractor(KeywordExtractorInterface):
    def __init__(self):
        self.language = "en"
        self.max_ngram_size = 3
        self.deduplication_thresold = 0.9
        self.deduplication_algo = 'seqm'
        self.windowSize = 1
        self.numOfKeywords = 20
        
    def _extractor_init(self) -> yake.KeywordExtractor:
        return yake.KeywordExtractor(lan=self.language, 
                                     n=self.max_ngram_size, 
                                     dedupLim=self.deduplication_thresold, 
                                     dedupFunc=self.deduplication_algo, 
                                     windowsSize=self.windowSize, 
                                     top=self.numOfKeywords)

    def extract(self, text: str) -> List[Tuple[str, float]]:
        results = self. _extractor_init().extract_keywords(text,)
        return [{key: float(value)} for key, value in results]

