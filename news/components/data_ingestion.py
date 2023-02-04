import os, sys
from pandas import DataFrame
from news.logger import logging
from news.exception import NewsException
from news.entity.config_entity import DataIngestionConfig
from news.entity.artifact_entity import DataIngestionArtifact
from news.constants.training_pipeline_constants import SCHEMA_FILE_PATH, DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO, ARTIFACTS_DIR
from news.utils.main_utils import read_yaml_file
from news.data_access.news_data import NewsData
from sklearn.model_selection import train_test_split

class DataIngestion:
    def __init__(self, data_ingestion_config:DataIngestionConfig):
        try:
            self.data_ingestion_config = data_ingestion_config
            self.schema_config = read_yaml_file(SCHEMA_FILE_PATH)
        except Exception as e:
            raise NewsException(e, sys)
    def export_data_into_feature_store(self)-> DataFrame:
        """
        Export Cassandra DB Table Data as Data Frame to feature store
        """
        try:
            logging.info("Start :: Exporting Data From Cassandra DB to feature store")
            news_data = NewsData()
            dataframe = news_data.export_database_data_as_dataframe()
            feature_store_file_path = self.data_ingestion_config.feature_store_file_path

            dir_path = os.path.dirname(feature_store_file_path)
            os.makedirs(dir_path, exist_ok=True)

            dataframe.to_csv(feature_store_file_path, index=False, header=True)
            logging.info("End :: Export Data From Cassandra DB to feature store")
            return dataframe
        except Exception as e:
            raise NewsException(e, sys)
    def split_data_as_train_test(self, dataframe:DataFrame) -> None:
        """
        Feature Store Dataset Will be split into train and test file
        """
        try:
            train_df, test_df = train_test_split(dataframe, test_size = DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO)
            logging.info("Dataset Splitted to Train and Test Succesfully")

            dir_path = os.path.dirname(self.data_ingestion_config.train_file_path)
            os.makedirs(dir_path, exist_ok=True)

            train_df.to_csv(self.data_ingestion_config.train_file_path, index=False, header=True)
            test_df.to_csv(self.data_ingestion_config.test_file_path, index=False, header=True)
            logging.info("Dataset been splitted to Train and Test")
        except Exception as e:
            raise NewsException(e, sys)

    def initiate_data_ingestion(self) -> DataIngestionArtifact:
        try:
            dataframe = self.export_data_into_feature_store()
            self.split_data_as_train_test(dataframe=dataframe)
            data_ingestion_artifact = DataIngestionArtifact(
                                        train_file_path=self.data_ingestion_config.train_file_path,
                                        test_file_path= self.data_ingestion_config.test_file_path
                                        ) 
            print(data_ingestion_artifact)
            return data_ingestion_artifact
        except Exception as e:
            raise NewsException(e, sys)