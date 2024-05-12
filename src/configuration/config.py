from src.constants import *
from src.entity.config import DataIngestionConfig, LoadModelConfig, TrainingConfig, EvaluationConfig
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
    
    def get_train_model_config(self) -> TrainingConfig:
        data_ingestion_config = self.config.data_ingestion
        load_model_config = self.config.load_model
        train_model_config = self.config.training_model
        create_directories([train_model_config.root_dir])

        train_model_config = TrainingConfig(root_dir=Path(train_model_config.root_dir),
                                            base_model_path=Path(load_model_config.model_path),
                                            trained_model_path=Path(train_model_config.model_path),
                                            training_data=Path(data_ingestion_config.train_data_dir),
                                            epochs=self.params.EPOCHS,
                                            batch_size=self.params.BATCH_SIZE,
                                            patience=self.params.PATIENCE,
                                            agumentation=self.params.AUGMENTATION,
                                            image_size=self.params.IMAGE_SIZE)
        return train_model_config
    
    def get_evaluation_config(self) -> EvaluationConfig:
        data_ingestion_config = self.config.data_ingestion
        train_model_config = self.config.training_model

        evaluation_config = EvaluationConfig(model_path=Path(train_model_config.model_path), 
                                             training_data=Path(data_ingestion_config.train_data_dir),
                                             all_params=self.params,
                                             mlflow_uri="https://dagshub.com/Sandeep-Pasumarthi/Chest-Disease-Classification.mlflow",
                                             image_size=self.params.IMAGE_SIZE,
                                             batch_size=self.params.BATCH_SIZE)
        return evaluation_config
