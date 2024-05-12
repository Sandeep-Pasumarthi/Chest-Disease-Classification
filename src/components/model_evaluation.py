from src.entity.config import EvaluationConfig
from src.utils.file import save_json_file
from src.utils.directories import create_directories
from src import logger

from urllib.parse import urlparse
from pathlib import Path

import mlflow
import mlflow.keras
import tensorflow as tf


class ModelEvaluation:
    def __init__(self, config: EvaluationConfig):
        self.config = config
    
    def data_generator(self):
        logger.info(f"Generating validation generator")
        self.data_generator = tf.keras.preprocessing.image.ImageDataGenerator(
            samplewise_center=True,
            samplewise_std_normalization=True,
            rescale=1./255,
            shear_range=0.1,
            zoom_range=0.1,
            horizontal_flip=True,
            vertical_flip=True,
            validation_split=0.2
        )

        dataflow_kwargs = dict(
            target_size = self.config.image_size[:-1],
            batch_size = self.config.batch_size,
            interpolation = "bilinear"
        )

        self.validation_generator = self.data_generator.flow_from_directory(
            self.config.training_data,
            subset="validation",
            shuffle=True,
            seed=17,
            **dataflow_kwargs
        )
        logger.info(f"Generated validation generator")
    
    def load_model(self):
        logger.info(f"Loading Model from {self.config.model_path}")
        self.model = tf.keras.models.load_model(self.config.model_path)
        logger.info(f"Model loaded from {self.config.model_path}")
    
    def evaluate_model(self):
        logger.info(f"Evaluating Model")
        self.score = self.model.evaluate(self.validation_generator)
        logger.info(f"Model evaluated")
    
    def save_metrics(self):
        metrics = {"loss": self.score[0], "accuracy": self.score[1]}
        logger.info(f"Saving metrics to {Path('reports/metrics.json')}")
        create_directories([Path("reports/")])
        save_json_file(Path("reports/metrics.json"), metrics)
        logger.info(f"Metrics saved to {Path('reports/metrics.json')}")
    
    def log_to_mlflow(self):
        logger.info(f"Logging to MLFlow")
        mlflow.set_registry_uri(self.config.mlflow_uri)
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme

        with mlflow.start_run():
            mlflow.log_params(self.config.all_params)
            mlflow.log_metrics(
                {"loss": self.score[0], "accuracy": self.score[1]}
            )

            if tracking_url_type_store != "file":
                mlflow.keras.log_model(self.model, "model", registered_model_name="EfficientNetV2M")
            else:
                mlflow.keras.log_model(self.model, "model")
        logger.info(f"Logged to MLFlow")
