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
from airflow.operators.python_operator import PythonOperator # type:ignore

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
        SELECT * EXCEPT(Category, random), 
        FROM(
            SELECT *, RAND() as random
            FROM `{dataset_id}.{view_id}`
            WHERE Category = "{category}"
            ORDER BY random
        )
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

def filter_collection_names(collection_names:list)->list:
    collection_names = [name for name in collection_names if 'view' not in name]
    if collection_names:
        return collection_names
    else:
        return []
    
def transform():
    global db_name, uri
    
    yake = YakeKeywordExtractor()
    yake.max_ngram_size = 2
    keyword_extractor = KeywordExtractor(yake)
    logging.info("KEY WORDS EXTRACTOR INSTANCE HAS BEEN CREATED")
    
    try:
        dist_client = MongoDBClient(uri, db_name)
        logging.info("CONNECTED TO MONGO SUCCESSFULLY!")
        loader = Loader(dist_client)
        collection_names = dist_client.collections
        collection_names = filter_collection_names(collection_names)
        logging.info(f"collections found: {collection_names}")
    except Exception as e:
        logging.error(f"FILED TO CONNECT TO MONGO!\n{e}")
        return
    
    keywordsKey = "keywords" 
    for collection_name in collection_names:
        
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
            kewyword_score_pair = keyword_extractor.extract(text)
            keywords = [{"kw":key, "score":value} for key, value in kewyword_score_pair]
            
            updated_doc = {
                **doc, 
                keywordsKey: keywords
            }
            
            loader.update(collection_name, {'_id':doc['_id']}, updated_doc)

def create_view():
    client = MongoDBClient(uri, db_name)
    collection_names = client.collections
    
    existing_view_names = [name for name in collection_names if "view" in name]
    collection_names = filter_collection_names(collection_names)
    
    logging.info(f"existing views:{existing_view_names}")
    logging.info(f"Collection names:{collection_names}")
    
    interface = Loader(client)
    
    collection_name='' #placeholder
    keyword_freq_pipeline = [
        { "$unwind": "$keywords" },
        {
            "$group": {
                "_id": "$keywords.kw",
                "avg_score": { "$avg": "$keywords.score" },
                "freq": { "$sum": 1 }
            }
        },
        {
            "$project": {
                "_id": 0,
                "keyword": "$_id",
                "avg_score": 1,
                "freq": 1
            }
        },
        { "$sort": { "freq": -1 } }
    ]
    for collection_name in collection_names:
        top_articles_pipeline=[
            {"$unwind": "$keywords"},
            {
                "$lookup": {
                    "from": f'{collection_name}_keywords_freq',
                    "localField": "keywords.kw",
                    "foreignField": "keyword",
                    "as": "keyword_freq"
                }
            },
            {
                "$addFields": {
                    "keywords.freq": { "$arrayElemAt": ["$keyword_freq.freq", 0] }
                }
            },
            {
                "$group": {
                    "_id": "$_id",
                    "title": { "$first": "$title" },
                    "body": { "$first": "$body" },
                    "score": { "$sum": "$keywords.freq" }
                }
            },
            { "$sort": { "score": -1 } },
            {
                "$project": {
                    "_id": 0,
                    "title": 1,
                    "body": 1,
                    "score": 1
                }
            }
        ]
    
        view_freq_name = f'{collection_name}_keywords_freq_view'
        if view_freq_name not in existing_view_names:
            interface.create_view(view_name=view_freq_name,
                                view_on=collection_name,
                                pipeline=keyword_freq_pipeline)
        
        view_top_name = f'{collection_name}_top_articles_view'
        if view_top_name not in existing_view_names:
            interface.create_view(view_name=view_top_name,
                                view_on=collection_name,
                                pipeline=top_articles_pipeline)
    
   

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
    
    create_view_task = PythonOperator(
        task_id='create_view_task',
        python_callable=create_view,
    )
    
    extract_load_task >> transform_task >> create_view_task