from src.constants import *
from src.entity.config import DataIngestionConfig
from src.utils.file import read_yaml_file
from src.utils.directories import create_directories


class ConfigurationManager:
    def __init__(self, config_file_path: str=CONFIG_FILE_PATH, params_file_path: str=PARAMS_FILE_PATH):
        self.config = read_yaml_file(config_file_path)
        self.params = read_yaml_file(params_file_path)

        create_directories([self.config.artifacts_root])
    
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(root_dir=config.root_dir,
                                                    source_url=config.source_url,
                                                    local_data_file=config.local_data_file,
                                                    unzip_dir=config.unzip_dir)
        return data_ingestion_config
