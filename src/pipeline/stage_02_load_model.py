from src.configuration.config import ConfigurationManager
from src.components.load_model import LoadModel
from src import logger


class LoadModelPipeLine:
    def __init__(self):
        pass

    def run(self):
        try:
            logger.info(f"In {__file__}: Intializing STAGE LoadModel")
            config_manager = ConfigurationManager()
            load_model_config = config_manager.get_load_model_config()
            load_model = LoadModel(config=load_model_config)
            load_model.download_pretrained_model()
            load_model.prepare_model()
            load_model.save_model()
            logger.info(f"In {__file__}: Completed STAGE LoadModel")
        except Exception as e:
            logger.error(f"Error in {__file__}: {e}")
            raise e
