from src.constants import *
from src.entity.config import DataIngestionConfig, LoadModelConfig
from src.utils.file import read_yaml_file
from src.utils.directories import create_directories

from pathlib import Path


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
    
    def get_load_model_config(self) -> LoadModelConfig:
        config = self.config.load_model
        create_directories([config.root_dir])

        load_model_config = LoadModelConfig(root_dir=Path(config.root_dir),
                                            model_path=Path(config.model_path),
                                            image_size=self.params.IMAGE_SIZE,
                                            learning_rate=self.params.LEARNING_RATE,
                                            include_top=self.params.INCLUDE_TOP,
                                            weights=self.params.WEIGHTS,
                                            classes=self.params.CLASSES)
        return load_model_config
