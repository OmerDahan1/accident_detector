from .utils import (crop_frame_by_detaction)
from server import ROBOFLOW_CLIENT as ROBOFLOW_CLIENT
from server import logger
from inference_sdk import InferenceConfiguration


class LicensePlateDetector:
    def __init__(self):
        pass

    def detact(self, image):
        try:
            result = ROBOFLOW_CLIENT.infer(image, model_id="np_detection-xgvjf/2")

        except Exception as e:
            # print(f"An error occurred during the external API call: {e}")
            logger.exception(f"An error occurred during the external API call: {e}")
            # Optionally log the error or handle it as needed
            return None  # or handle it in another appropriate way
        for prediction in result["predictions"]:
            res = crop_frame_by_detaction(image, prediction)
            return res
        return None

    def extract_license_plate_symbols(self, image):
        custom_configuration = InferenceConfiguration(confidence_threshold=0.6)
        try:
            with ROBOFLOW_CLIENT.use_configuration(custom_configuration):
                results = ROBOFLOW_CLIENT.infer(image, model_id="license-ocr-qqq6v/3")
        except Exception as e:
            logger.exception(f"An error occurred during the external API call: {e}")
            # print(f"An error occurred during the external API call: {e}")
            return None

        predictions = results["predictions"]
        predictions = sorted(predictions, key=lambda item: item['x'])
        symbols = [prediction["class"] for prediction in predictions]
        if len(symbols) > 0:
            logger.info(f"Extracted symbols: {symbols}")
        return symbols
