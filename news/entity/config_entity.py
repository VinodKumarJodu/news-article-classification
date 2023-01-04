import os
from datetime import datetime

from news.logger import logging
from news.exception import NewsException

from dataclasses import dataclass
from news.constants.training_pipeline_constants import PIPELINE_NAME, ARTIFACT_DIR, TRAIN_FILE_NAME, TEST_FILE_NAME, PREPROCESSING_OBJECT_FILE_NAME

class TrainingPipelineConfig:
    def __int__(self, timestamp=datetime.now()):
        timestamp = timestamp.strftime('%m_%d_%Y_%H_%M_%S')
        self.timestamp = timestamp
        self.pipeline_name: str = PIPELINE_NAME
        self.artifact_dir: str = os.path.join(ARTIFACT_DIR, timestamp)

class DataTransformationConfig:
    def __init__(self, training_pipeline_config:TrainingPipelineConfig):
        self.data_transformation_dir: str = os.path.join(artifact_dir, DATA_TRANSFORMATION_DIR_NAME)
        self.transformed_train_file_path: str = os.path.join(self.data_transformation_dir, DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR_NAME, TRAIN_FILE_NAME.replace("csv","npy"))
        self.transformed_test_file_path: str = os.path.join(self.data_transformation_dir, DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR_NAME, TEST_FILE.replace("csv","npy"))       
        self.transformed_object_file_path: str = os.path.join(self.data_transformation_dir, DATA_TRANSFORMATION_TRANSFRMED_OBJECT_DIR, PREPROCESSING_OBJECT_FILE_NAME)
        