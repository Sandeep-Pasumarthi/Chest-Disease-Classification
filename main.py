from src.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from src.pipeline.stage_02_load_model import LoadModelPipeLine
from src.pipeline.stage_03_train_model import TrainModelPipeline
from src.pipeline.stage_04_evaluate_model import ModelEvaluationPipeline
from src import logger


try:
    data_ingestion = DataIngestionPipeline()
    data_ingestion.run()
    load_model = LoadModelPipeLine()
    load_model.run()
    train_model = TrainModelPipeline()
    train_model.run()
    evaluate_model = ModelEvaluationPipeline()
    evaluate_model.run()
except Exception as e:
    logger.error(f"Error in {__file__}: {e}")
    raise e
