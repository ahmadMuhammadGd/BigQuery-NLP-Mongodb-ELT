from src.Config_parser import ConfigParser

global_config = ConfigParser("./pipeline_config/articlesPipelineConfig.json")

# BigQuery global variables
credential_path = global_config.get_credentials()["jsonBigQueryCredFilePath"]
bq_meta_data = global_config.get_bigquery_config()
project_id = bq_meta_data["projectId"]
dataset_id = bq_meta_data["datasetId"]
view_id = bq_meta_data["viewId"]

# MongoDB global variables
mongo_config = global_config.get_Mongo_config()
uri = mongo_config["uri"]
db_name = mongo_config["db_name"]