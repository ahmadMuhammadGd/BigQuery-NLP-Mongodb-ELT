import json
from typing import Any, Dict

class ConfigParser:
    def __init__(self, config_file_path: str):
        self.config_file_path = config_file_path
        self.config_data = self._load_config()

    def _load_config(self) -> Dict[str, Any]:
        with open(self.config_file_path, 'r') as file:
            return json.load(file)

    def get_credentials(self) -> Dict[str, Any]:
        return self.config_data.get('CREDENTIALS', {})

    def get_paths(self) -> Dict[str, Any]:
        return self.config_data.get('PATHS', {})

    def get_secrets(self) -> Dict[str, Any]:
        return self.config_data.get('SECRETS', {})
    
    def get_bigquery_config(self) -> Dict[str, Any]:
        return self.config_data.get('BIGQUERY', {})

    def get_Mongo_config(self) -> Dict[str, Any]:
        return self.config_data.get('MONGODB', {})
    
    def get_from_custome_config(self, section:str, key:str=None):
        if not key:
            return self.get_config(section)
        elif key:
            return self.config_data.get(section)[key]
    
    def get_config(self, section: str) -> Any:
        return self.config_data.get(section)
    