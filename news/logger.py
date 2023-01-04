import os
import logging
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.log"

LOG_FILE_PATH = os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(LOG_FILE_PATH, exist_ok=True)

# LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)
logging.basicConfig(
    filename = LOG_FILE_PATH,
    format = "[%(asctime)s: %(filename)s: %(funcName)s: %(module)s: %(levelname)s] %(message)s",
    level = logging.INFO
)