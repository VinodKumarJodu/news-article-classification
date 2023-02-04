import os
from datetime import datetime

from news.logger import logging
from news.exception import NewsException

from dataclasses import dataclass
from news.constants.training_pipeline_constants import PIPELINE_NAME, ARTIFACTS_DIR, FILE_NAME, TRAIN_FILE_NAME, TEST_FILE_NAME, PREPROCESSING_OBJECT_FILE_NAME
#Data Ingestion related Constants
from news.constants.training_pipeline_constants import DATA_INGESTION_DIR_NAME, DATA_INGESTION_FEATURE_STORE_DIR, DATA_INGESTION_INGESTED_DIR, DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO

class TrainingPipelineConfig:
    def __int__(self, timestamp=datetime.now()):
        timestamp = timestamp.strftime('%m_%d_%Y_%H_%M_%S')
        self.pipeline_name: str = PIPELINE_NAME
        self.artifact_dir: str = os.path.join(ARTIFACTS_DIR, timestamp)
        # self.timestamp: str = timestamp

class DataIngestionConfig:
    def __init__(self, training_pipeline_config:TrainingPipelineConfig):
        self.data_ingestion_dir:str = os.path.join(training_pipeline_config.artifact_dir, DATA_INGESTION_DIR_NAME)
        self.feature_store_file_path:str = os.path.join(self.data_ingestion_dir,DATA_INGESTION_FEATURE_STORE_DIR, FILE_NAME)
        self.train_file_path: str = os.path.join(self.data_ingestion_dir,DATA_INGESTION_INGESTED_DIR, TRAIN_FILE_NAME)
        self.test_file_path: str = os.path.join(self.data_ingestion_dir,DATA_INGESTION_INGESTED_DIR, TEST_FILE_NAME)
        self.train_test_split_ration: float = DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO

# class DataTransformationConfig:
#     def __init__(self, training_pipeline_config:TrainingPipelineConfig):
#         self.data_transformation_dir: str = os.path.join(artifact_dir, DATA_TRANSFORMATION_DIR_NAME)
#         self.transformed_train_file_path: str = os.path.join(self.data_transformation_dir, DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR_NAME, TRAIN_FILE_NAME.replace("csv","npy"))
#         self.transformed_test_file_path: str = os.path.join(self.data_transformation_dir, DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR_NAME, TEST_FILE.replace("csv","npy"))       
#         self.transformed_object_file_path: str = os.path.join(self.data_transformation_dir, DATA_TRANSFORMATION_TRANSFRMED_OBJECT_DIR, PREPROCESSING_OBJECT_FILE_NAME)
        