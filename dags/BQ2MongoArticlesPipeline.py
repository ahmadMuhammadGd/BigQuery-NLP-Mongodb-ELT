import sys, os 

sys.path.insert(1, os.path.join(os.getcwd()))

import logging
logging.basicConfig(level=logging.INFO) 

from src.TabularSource.Extractor import Extractor
from src.TabularSource.BigQuery_client import BigQueryClient
from src.NoSQLDist.Loader import Loader
from src.NoSQLDist.Mongodb_client import MongoDBClient
from src.KeywordExtraction.KeywordExtractor import KeywordExtractor
from src.KeywordExtraction.Yake import YakeKeywordExtractor
from dags.globalVaribles.BQ2Mongo import *

from airflow import DAG
from airflow.operators.python_operator import PythonOperator # type: ignore
from datetime import datetime


def extractArticles():
    global credential_path, project_id, dataset_id, view_id
 
    logging.info("FOUND CREDENTIAlS!")

    client = BigQueryClient(
        credentials_path= credential_path,
        project_id= project_id
        )
    extractor = Extractor(client)
    
    logging.info("EXTRACTING CATEGORIES LIST")
    categories = extractor.extract(
        f"""
        SELECT DISTINCT Category 
        FROM {dataset_id}.{view_id};
        """)

    categories = [list(pair.values())[0] for pair in categories]
    
    logging.info("EXTRACTING DATA ON CATEGORY")
    return {category: extractor.extract(f"""
            SELECT * EXCEPT(Category)
            FROM {dataset_id}.{view_id}
            WHERE Category = "{category}"
            LIMIT 10;
        """) for category in categories}
            

def extract_load():
    global db_name, uri
    content = extractArticles()
    dist_client = MongoDBClient(uri, db_name)
    for category in content:
        print(category)
        data = content[category]
        loader = Loader(dist_client)
        loader.load_incremental(
            collection_name=category,
            data=data,
            source_PK="filename",
            dist_PK="filename")


def transform():
    global db_name, uri
    
    yake = YakeKeywordExtractor()
    yake.max_ngram_size = 2
    extractor = KeywordExtractor(yake)
    logging.info("KEY WORDS EXTRACTOR INSTANCE HAS BEEN CREATED")
    
    try:
        dist_client = MongoDBClient(uri, db_name)
        logging.info("CONNECTED TO MONGO SUCCESSFULLY!")
        loader = Loader(dist_client)
        collections = dist_client.collections
        logging.info(f"collections found: {collections}")
    except Exception as e:
        logging.error(f"FILED TO CONNECT TO MONGO!\n{e}")
        return
    
    keywordsKey = "keywords" 
    for collection_name in collections:
        
        query = {keywordsKey: {"$exists": False}}
        results = loader.find(
            collection_name=collection_name,
            filter_query=query
            )
        logging.info(f"results:\n{results}")
        
        if not results:
            logging.info(f"{collection_name}: Every thing is up to date")
            continue
        
        for doc in results:
            text = doc.get('body', '')  
            keywords = extractor.extract(text)
            
            updated_doc = {
                **doc, 
                keywordsKey: keywords
            }
            
            loader.update(collection_name, {'_id':doc['_id']}, updated_doc)



default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2021, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
}

with DAG('Articles_Keywords_ELT',
        default_args=default_args,
        max_active_runs=2,
        catchup=False,
        ) as dag:
    
    extract_load_task = PythonOperator(
        task_id='extract_load_task',
        python_callable=extract_load,
    )
    
    transform_task = PythonOperator(
        task_id='transform_task',
        python_callable=transform,
    )
    
    extract_load_task >> transform_task