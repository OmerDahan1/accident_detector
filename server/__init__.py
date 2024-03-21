from inference_sdk import InferenceHTTPClient
import os

ROBOFLOW_API_KEY = os.environ.get("ROBOFLOW_API_KEY")
ROBOFLOW_CLIENT = InferenceHTTPClient(
    api_url="https://detect.roboflow.com",
    api_key=ROBOFLOW_API_KEY
)

CALLER_API_KEY = os.environ.get("CALLER_API_KEY")
CALLER_SECRET_KEY = os.environ.get("CALLER_SECRET_KEY")

