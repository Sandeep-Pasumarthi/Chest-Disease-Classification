from src.entity.config import LoadModelConfig
from src import logger

import tensorflow as tf


class LoadModel:
    def __init__(self, config: LoadModelConfig):
        self.config = config
    
    def download_pretrained_model(self):
        logger.info("Loading model")
        self.model = tf.keras.applications.EfficientNetV2M(
            input_shape=self.config.image_size,
            weights=self.config.weights,
            include_top=self.config.include_top
        )
        logger.info("Model loaded")
    
    def prepare_model(self):
        logger.info("Preparing model")
        for layer in self.model.layers:
            layer.trainable = False
        
        flatten = tf.keras.layers.Flatten()(self.model.output)

        layer1 = tf.keras.layers.Dense(units=64, activation="relu")(flatten)
        layer2 = tf.keras.layers.Dense(units=32, activation="relu")(layer1)
        layer3 = tf.keras.layers.Dense(units=self.config.classes, activation="softmax")(layer2)

        self.model = tf.keras.Model(inputs=self.model.input, outputs=layer3)
        self.model.compile(
            optimizer=tf.keras.optimizers.Adam(learning_rate=self.config.learning_rate),
            loss=tf.keras.losses.CategoricalCrossentropy(),
            metrics=["accuracy"]
        )
        logger.info("Model prepared")
    
    def save_model(self):
        logger.info(f"Saving model at {self.config.model_path}")
        self.model.save(self.config.model_path)
        logger.info(f"Model saved at {self.config.model_path}")
