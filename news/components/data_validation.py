import os, sys
import pandas as pd
from news.logger import logging
from news.exception import NewsException
from typing import List

from news.entity.config_entity import DataValidationConfig
from news.entity.artifact_entity import DataValidationArtifact, DataIngestionArtifact
from news.constants.training_pipeline_constants import SCHEMA_FILE_PATH, TARGET_COLUMN
from news.utils.main_utils import read_yaml_file, write_yaml_file

class DataValidation:
    def __init__(self, data_ingestion_artifact:DataIngestionArtifact, data_validation_config:DataValidationConfig):
        try:
            self.data_ingestion_artifact =  data_ingestion_artifact
            self.data_validation_config = data_validation_config
            self._schema_config = read_yaml_file(SCHEMA_FILE_PATH) 
            self.validation_results = {
                                        "validate_number_of_columns": None,
                                        "column_name_validation": None,
                                        "datatype_validation": None,
                                        "target_label_validation": None
                                      }
        except Exception as e:
            raise NewsException(e, sys)
    
    def validate_number_of_columns(self, dataframe:pd.DataFrame)-> bool:
        try:
            number_of_columns = len(self._schema_config['columns'])
            logging.info(f"Required Number of Columns: {number_of_columns}")
            logging.info(f"Number of COlumns in the Dataframe:{len(dataframe.columns)}")
            if len(dataframe.columns) == number_of_columns:
                return True
            return False

        except Exception as e:
            raise NewsException(e, sys)

    def column_name_validation(self, dataframe)-> bool:
        try:
            excpected_columns = [column['name'] for column in self._schema_config['columns']]
            if set(dataframe.columns) != set(excpected_columns):
                return False
            return True
        except Exception as e:
            raise NewsException(e, sys)

    def datatype_validation(self, dataframe)-> bool:
        try:
            columns = {column['name']: column['type'] for column in self._schema_config['columns']}
            for column, expected_type in columns.items():
                if dataframe[column].dtypes != expected_type:
                    return False
            return True
        except Exception as e:
            raise NewsException(e, sys)
    
    def target_label_validation(self, dataframe, target)-> bool:
        try:
            expected_labels = ['politics', 'business', 'entertainment', 'tech', 'sport']
            if set(dataframe[target].unique()) != set(expected_labels):
                return False
            return True
        except Exception as e:
            raise NewsException(e, sys)

    def duplicate_articleids(self, dataframe)-> List[int]:
        duplicates = dataframe[dataframe.duplicated(subset='ArtcleId')]['ArticleId'].values
        return list(duplicates)

    @staticmethod
    def read_data(file_path)-> pd.DataFrame:
        try:
            return pd.read_csv(file_path)
        except Exception as e:
            raise NewsException(e,sys)

    def initiate_data_validation(self)->DataValidationArtifact:
        try:
            train_file_path = self.data_ingestion_artifact.train_file_path
            test_file_path = self.data_ingestion_artifact.test_file_path

            train_df = DataValidation.read_data(train_file_path)
            test_df = DataValidation.read_data(test_file_path)

            self.validation_results['validate_number_of_columns'] = self.validate_number_of_columns(train_df)
            self.validation_results['column_name_validation'] = self.column_name_validation(train_df)
            self.validation_results['datatype_validation'] = self.datatype_validation(train_df)
            self.validation_results['target_label_validation'] = self.target_label_validation(train_df,TARGET_COLUMN)

            validation_report_path = self.data_validation_config.validation_report_path
            dir_path = os.path.dirname(validation_report_path)
            os.makedirs(dir_path, exist_ok=True)

            write_yaml_file(file_path=validation_report_path,content=self.validation_results)
            data_validation_artifact = DataValidationArtifact(
                validation_results= self.validation_results,
                valid_train_file_path= self.data_ingestion_artifact.train_file_path,
                valid_test_file_path= self.data_ingestion_artifact.test_file_path,
                invalid_train_file_path= None,
                invalid_test_file_path= None
            )
            return data_validation_artifact
            
        except Exception as e:
            raise NewsException(e, sys)
