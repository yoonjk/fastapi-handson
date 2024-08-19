import logging 
import sys
from time import time
from fastapi import Request

# get logger
logger = logging.getLogger()

formatter = logging.Formatter(fmt = "%(asctime)s - %(levelname)s - %(message)s")

# set handler
stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setFormatter(formatter)

# add handlers to the logger
logger.handlers = [stream_handler]

# set log-level
logger.setLevel(logging.INFO)
