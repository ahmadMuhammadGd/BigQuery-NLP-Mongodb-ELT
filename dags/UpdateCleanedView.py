
import sys, os 
sys.path.insert(1, os.path.join(os.getcwd()))

from globalVaribles.CleanedArticleView import *
from src.TabularSource.BigQuery_client import BigQueryClient
from src.TabularSource.Extractor import Extractor
from datetime import datetime

from airflow import DAG
from airflow.operators.python_operator import PythonOperator # type: ignore


def update_view():
    global project_id, credential_path, dataset_id, view_id
    client = BigQueryClient(project_id=project_id,
                            credentials_path=credential_path)
    extractor = Extractor(client=client)
    
    extractor.execute_query(query=f"""
    CREATE SCHEMA IF NOT EXISTS `{project_id}.{dataset_id}`;
    
    CREATE OR REPLACE VIEW `{project_id}.{dataset_id}.{view_id}` AS (
    SELECT * EXCEPT(row_number) FROM (
        SELECT
            *,
            ROW_NUMBER() OVER(PARTITION BY body ORDER BY body) AS row_number
        FROM 
            `bigquery-public-data.bbc_news.fulltext`
        )
    WHERE row_number = 1
    );
    """)


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2021, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
}

with DAG('Update_view',
        default_args=default_args,
        max_active_runs=2,
        catchup=False,
        ) as dag:
    update_view_task = PythonOperator(
        task_id='update_view_task',
        python_callable=update_view,
    )
    update_view_task
