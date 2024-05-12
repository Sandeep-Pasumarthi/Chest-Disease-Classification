from src.configuration.config import ConfigurationManager
from src.components.model_evaluation import ModelEvaluation
from src import logger


class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def run(self):
        try:
            logger.info(f"In {__file__}: Intializing STAGE ModelEvaluation")
            config_manager = ConfigurationManager()
            model_evaluation_config = config_manager.get_evaluation_config()
            model_evaluation = ModelEvaluation(config=model_evaluation_config)
            model_evaluation.data_generator()
            model_evaluation.load_model()
            model_evaluation.evaluate_model()
            model_evaluation.save_metrics()
            model_evaluation.transfer_to_model_dir()
            model_evaluation.log_to_mlflow()
            logger.info(f"In {__file__}: Completed STAGE ModelEvaluation")
        except Exception as e:
            logger.error(f"In {__file__}: Error while running STAGE ModelEvaluation: {e}")
            raise e


if __name__ == "__main__":
    try:
        model_evaluation_pipeline = ModelEvaluationPipeline()
        model_evaluation_pipeline.run()
    except Exception as e:
        logger.error(f"Error in {__file__}: {e}")
        raise e
