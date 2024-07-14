from pymongo import MongoClient
from src.TabularSource.Extractor import Extractor
from src.TabularSource.BigQuery_client import BigQueryClient 
from src.Config_parser import ConfigParser

global_config = ConfigParser("pipeline_config/config.json")

def extract(query):
    global global_config
    credential_path = global_config.get_credentials() 
    project_id = global_config.get_bigquery_config()["projectId"] 
    client = BigQueryClient(
        credentials_path= credential_path,
        project_id= project_id
        )
    extractor = Extractor(client)
    return extractor.extract(query)

def load(data:dict):
    client = MongoClient()
    db = client['article_keywords']
    