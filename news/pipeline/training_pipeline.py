import os, sys
from news.logger import logging
from news.exception import NewsException
from news.entity.config_entity import TrainingPipelineConfig, DataIngestionConfig
from news.entity.artifact_entity import DataIngestionArtifact
from news.components.data_ingestion import DataIngestion

class TrainingPipeline:
    def __init__(self):
        self.training_pipeline_config = TrainingPipelineConfig()
    
    def start_data_ingestion(self)-> DataIngestionArtifact:
        try:
            logging.info("Starting Data Ingestion")
            data_ingestion_config = DataIngestionConfig(training_pipeline_config=self.training_pipeline_config)
            data_ingestion = DataIngestion(data_ingestion_config = data_ingestion_config)
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            return data_ingestion_artifact
        except Exception as e:
            raise NewsException(e, sys)

    def run_pipeline(self):
        try:
            data_ingestion_artifact = self.start_data_ingestion()
        except Exception as e:
            raise NewsException(e, sys)