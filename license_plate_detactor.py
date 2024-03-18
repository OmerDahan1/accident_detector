from inference_sdk import InferenceHTTPClient
from utils import crop_frame_by_detaction
from roboflow_client import CLIENT as CLIENT


def detact_license_plate(image):
    result = CLIENT.infer(image, model_id="np_detection-xgvjf/2")
    for prediction in result["predictions"]:
        res = crop_frame_by_detaction(image, prediction)
        return res
    return None


def extract_license_plate_symbols(image):
    results = CLIENT.infer(image, model_id="license-ocr-qqq6v/1")
    predictions = results["predictions"]
    predictions = sorted(predictions, key=lambda item: item['x'])
    symbols = [prediction["class"] for prediction in predictions]
    return symbols
