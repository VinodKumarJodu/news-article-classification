import os, sys
import yaml
from news.logger import logging
from news.exception import NewsException
import numpy as np
import dill


def read_yaml_file(file_path:str) -> dict:
    try:
        logging.info("Reading Schema File :: START")
        with open(file_path,"rb") as yaml_file:
            return yaml.safe_load(yaml_file) 
        logging.info("Succesfully Read Yaml File:: END")
    except Exception as e:
        raise NewsException(e, sys)