from src.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from src import logger


try:
    data_ingestion = DataIngestionPipeline()
    data_ingestion.run()
except Exception as e:
    logger.error(f"Error in {__file__}: {e}")
    raise e
