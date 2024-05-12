from src.configuration.config import ConfigurationManager
from src.components.train_model import TrainModel
from src import logger


class TrainModelPipeline:
    def __init__(self):
        pass

    def run(self):
        try:
            logger.info(f"In {__file__}: Intializing STAGE TrainModel")
            config_manager = ConfigurationManager()
            train_model_config = config_manager.get_train_model_config()

            train_model = TrainModel(config=train_model_config)
            train_model.get_model()
            train_model.train_validation_generator()
            train_model.call_backs()
            train_model.train()
            train_model.save_model()
            logger.info(f"In {__file__}: Completed STAGE TrainModel")
        except Exception as e:
            logger.error(f"Error in {__file__}: {e}")
            raise e


if __name__ == "__main__":
    try:
        train_model_pipeline = TrainModelPipeline()
        train_model_pipeline.run()
    except Exception as e:
        logger.error(f"Error in {__file__}: {e}")
        raise e
