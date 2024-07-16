from google.cloud import bigquery
from google.oauth2 import service_account
from src.TabularSource.base import TabularSourceExtractorInterface

class BigQueryClient(TabularSourceExtractorInterface):
    def __init__(self, project_id: str, credentials_path: str = None):
        self.client = self._create_client(project_id, credentials_path)

    def _create_client(self, project_id: str, credentials_path: str):
        if credentials_path:
            credentials = service_account.Credentials.from_service_account_file(credentials_path)
            return bigquery.Client(project=project_id, credentials=credentials)
        return bigquery.Client(project=project_id)

    def execute_query(self, query: str)->list[dict]:
        query_job = self.client.query(query)
        return [dict(row.items()) for row in query_job]
