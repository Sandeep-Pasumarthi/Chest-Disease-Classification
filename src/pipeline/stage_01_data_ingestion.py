from src.configuration.config import ConfigurationManager
from src.components.data_ingestion import DataIngestion
from src import logger


class DataIngestionPipeline:
    def __init__(self):
        pass

    def run(self):
        try:
            logger.info(f"In {__file__}: Intializing STAGE DataIngestion")
            config = ConfigurationManager()
            data_ingestion_config = config.get_data_ingestion_config()
            data_ingestion = DataIngestion(config=data_ingestion_config)
            data_ingestion.download_file()
            data_ingestion.unzip_dir()
            logger.info(f"In {__file__}: Completed STAGE DataIngestion")
        except Exception as e:
            logger.error(f"In {__file__}:\n{e}")
            raise e


if __name__ == "__main__":
    try:
        data_ingestion = DataIngestionPipeline()
        data_ingestion.run()
    except Exception as e:
        logger.error(f"Error in {__file__}: {e}")
        raise e
