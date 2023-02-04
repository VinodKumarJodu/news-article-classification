import os

# Defining Common Constants
TARGET_COLUMN = "Category"
PIPELINE_NAME = "news"
ARTIFACTS_DIR = "artifacts"
FILE_NAME = "news_articles.csv"
TRAIN_FILE_NAME = "train.csv"
TEST_FILE_NAME = "test.csv"

PREPROCESSING_OBJECT_FILE_NAME = "preprocessing.pkl"
SCHEMA_FILE_PATH = os.path.join("config","schema.yaml")

"""
Defining Data Ingestion Related Constants :: DATA_INGESTION
"""
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_INGESTION_INGESTED_DIR: str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO: float = 0.2


"""
Defining Data Validation Related Constants:: DATA_VALIDATION
"""
DATA_VALIDATION_DIR_NAME: str = "data_validation"
DATA_VALIDATION_VALID_DIR: str = "validated"
DATA_VALIDATION_INVALID_DIR: str = "invalid"


"""
Defining Data Transformation Related Constants & Starts with DATA_TRANSFORMATION 
"""
DATA_TRANSFORMATION_DIR_NAME: str = "data_transformation"
DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR_NAME: str = "transformation"
DATA_TRANSFORMATION_TRANSFRMED_OBJECT_DIR: str = "transformed_object"