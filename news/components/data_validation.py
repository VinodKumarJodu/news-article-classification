import os, sys
import pandas as pd
from news.logger import logging
from news.exception import NewsException

from news.entity.config_entity import DataValidationConfig
from news.entity.artifact_entity import DataValidationArtifact, DataIngestionArtifact
from news.constants.training_pipeline_constants import SCHEMA_FILE_PATH
from news.utils.main_utils import read_yaml_file

class DataValidation:
    def __init__(self, data_ingestion_artifact:DataIngestionArtifact, data_validation_config:DataValidationConfig):
        try:
            self.data_ingestion_artifact =  data_ingestion_artifact
            self.data_validation_config = data_validation_config
            self._schema_config = read_yaml_file(SCHEMA_FILE_PATH) 
        except Exception as e:
            raise NewsException(e, sys)

    def initiate_data_validation(self)->DataValidationArtifact:
        try:
            train_file_path = self.data_ingestion_artifact.train_file_path
            test_file_path = self.data_ingestion_artifact.test_file_path
        except Exception as e:
            raise NewsException(e, sys)
