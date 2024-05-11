from src.entity.config import DataIngestionConfig
from src import logger

import gdown
import zipfile
import os


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
    
    def download_file(self) -> None:
        try:
            data_url = self.config.source_url
            download_file = self.config.local_data_file
            logger.info(f"Downloading {data_url} to {download_file}")
            file_id = data_url.split("/")[-2]
            prefix = 'https://drive.google.com/uc?/export=download&id='
            gdown.download(prefix+file_id, download_file)
            logger.info(f"Downloaded {data_url} to {download_file}")
        except Exception as e:
            raise e
    
    def unzip_dir(self) -> None:
        try:
            unzip_dir = self.config.unzip_dir
            os.makedirs(unzip_dir, exist_ok=True)

            with zipfile.ZipFile(self.config.local_data_file) as f:
                logger.info(f"Extracting {self.config.local_data_file} to {unzip_dir}")
                f.extractall(unzip_dir)
                logger.info(f"Extracted {self.config.local_data_file} to {unzip_dir}")
        except Exception as e:
            raise e
