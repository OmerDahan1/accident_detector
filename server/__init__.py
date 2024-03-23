from inference_sdk import InferenceHTTPClient
import os

ROBOFLOW_API_KEY = os.environ.get("ROBOFLOW_API_KEY")
ROBOFLOW_CLIENT = InferenceHTTPClient(
    api_url="https://detect.roboflow.com",
    api_key=ROBOFLOW_API_KEY
)

CALLER_API_KEY = os.environ.get("CALLER_API_KEY")
CALLER_SECRET_KEY = os.environ.get("CALLER_SECRET_KEY")

import logging.config
from .logging_config import LOGGING_CONFIG  # Import the logging configuration

# Apply the logging configuration
logging.config.dictConfig(LOGGING_CONFIG)

# Obtain a reference to the configured logger
logger = logging.getLogger('server_logger')