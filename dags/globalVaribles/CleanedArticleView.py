from src.Config_parser import ConfigParser

global_config = ConfigParser("./pipeline_config/sourceCleanedViewConfig.json")

# BigQuery global variables
credential_path = global_config.get_credentials()["jsonBigQueryCredFilePath"]
bq_meta_data = global_config.get_bigquery_config()
project_id = bq_meta_data["projectId"]
dataset_id = bq_meta_data["datasetId"]
view_id = bq_meta_data["viewId"]