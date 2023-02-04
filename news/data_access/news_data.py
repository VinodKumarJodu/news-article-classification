import os, sys
from typing import Optional
from news.exception import NewsException
from news.logger import logging
import numpy as np
import pandas as pd
import json
from news.configurations.cassandra_db_connection import CassandraDBConnection
from news.constants.database import KEY_SPACE, TABLE_NAME_TRAIN, TABLE_NAME_TEST

class NewsData:
    def __init__(self):
        try:
            cassandra = CassandraDBConnection()
            session = cassandra.connect()
        except Exception as e:
            raise NewsException(e,sys)
    
    def export_database_data_as_dataframe(self)-> pd.DataFrame:
        try:
            logging.info("Connecting to the Cassandra Database Initiated")
            cassandra = CassandraDBConnection()
            session = cassandra.connect()
            query = f"SELECT * FROM {KEY_SPACE}.{TABLE_NAME_TRAIN}"
            rows = session.execute(query)
            logging.info("Connection to Cassandra Database Succesful")
            df = pd.DataFrame(list(rows))
            return df
        except Exception as e:
            logging.info("Connection to Cassandra Database is Failed")
            raise NewsException(e, sys)
