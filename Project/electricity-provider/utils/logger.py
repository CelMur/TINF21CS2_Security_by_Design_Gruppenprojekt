import os
import logging
from sys import stdout
from logging.handlers import TimedRotatingFileHandler
from datetime import datetime
import pytz
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
log_directory = "logs"
os.makedirs(log_directory, exist_ok=True)

logging.basicConfig(handlers=[logging.StreamHandler(stdout)],
                    level=logging.DEBUG,
                    format=LOG_FORMAT,
                    datefmt='%d/%m/%Y %H:%M:%S')

current_date = datetime.now(pytz.timezone('Europe/Berlin')).strftime("%Y-%m-%d")
logfile_name = os.path.join(log_directory, f"logfile_{current_date}.log")

file_handler = TimedRotatingFileHandler(logfile_name, when='midnight', interval=1, backupCount=0)
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging.Formatter(LOG_FORMAT))

logger = logging.getLogger()
logger.addHandler(file_handler)
