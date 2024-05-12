from src.entity.config import TrainingConfig
from src import logger

import tensorflow as tf


class TrainModel:
    def __init__(self, config: TrainingConfig):
        self.config = config
    
    def get_model(self):
        logger.info(f"Loading Model from {self.config.base_model_path}")
        self.model = tf.keras.models.load_model(self.config.base_model_path)
        logger.info(f"Model loaded from {self.config.base_model_path}")
    
    def train_validation_generator(self):
        logger.info(f"Generating training validation generator")
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

        self.train_generator = self.data_generator.flow_from_directory(
            self.config.training_data,
            subset="training",
            shuffle=True,
            seed=17,
            **dataflow_kwargs
        )
        logger.info(f"Generated train generator")

        self.validation_generator = self.data_generator.flow_from_directory(
            self.config.training_data,
            subset="validation",
            shuffle=True,
            seed=17,
            **dataflow_kwargs
        )
        logger.info(f"Generated validation generator")
    
    def call_backs(self):
        logger.info("Generating Callbacks for training")
        self.early_stopping = tf.keras.callbacks.EarlyStopping(
            monitor="val_loss",
            patience=self.config.patience,
            mode="min",
            restore_best_weights=True
        )
        logger.info("Generated Callbacks for training")
    
    def train(self):
        logger.info(f"Training Model started")
        self.steps_per_epoch = self.train_generator.samples // self.train_generator.batch_size
        self.validation_steps = self.validation_generator.samples // self.validation_generator.batch_size

        self.model.fit(
            self.train_generator,
            epochs=self.config.epochs,
            steps_per_epoch=self.steps_per_epoch,
            validation_data=self.validation_generator,
            validation_steps=self.validation_steps,
            callbacks = [self.early_stopping]
        )
        logger.info(f"Training Model completed")
    
    def save_model(self):
        logger.info(f"Saving model to {self.config.trained_model_path}")
        self.model.save(self.config.trained_model_path)
        logger.info(f"Saved model to {self.config.trained_model_path}")
