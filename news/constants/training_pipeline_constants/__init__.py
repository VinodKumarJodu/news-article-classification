import os

# Defining Common Constants
TARGET_COLUMN = "category"
PIPELINE_NAME = "news"
ARTIFACT_DIR = "artifacts"

TRAIN_FILE_NAME = "train.csv"
TEST_FILE_NAME = "test.csv"
PREPROCESSING_OBJECT_FILE_NAME = "preprocessing.pkl"
"""
Defining Data Transformation Related Constants & Starts with DATA_TRANSFORMATION 
"""
DATA_TRANSFORMATION_DIR_NAME: str = "data_transformation"
DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR_NAME: str = "transformation"
DATA_TRANSFORMATION_TRANSFRMED_OBJECT_DIR: str = "transformed_object"