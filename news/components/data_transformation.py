import os, sys
import numpy as np 
import pandas as pd 

from news.logger import logging
from news.exception import NewsException

from news.entity.config_entity import DataTransformationConfig
from news.entity.artifact_entity import DataTransformationConfig

class DataTransformation:
    def __init__(self, data_transformation_config: DataTransformationConfig):
        try:
            self.data_transformation_config = data_transformation_config
            
        except Exception as e:
            raise NewsException(e, sys)

