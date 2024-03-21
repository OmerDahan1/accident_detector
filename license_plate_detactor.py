# from server.utils import crop_frame_by_detaction
# from roboflow_client import ROBOFLOW_CLIENT as ROBOFLOW_CLIENT
#
# def detact_license_plate(image):
#     result = ROBOFLOW_CLIENT.infer(image, model_id="np_detection-xgvjf/2")
#     for prediction in result["predictions"]:
#         res = crop_frame_by_detaction(image, prediction)
#         return res
#     return None
#
#
# def extract_license_plate_symbols(image):
#     results = ROBOFLOW_CLIENT.infer(image, model_id="license-ocr-qqq6v/1")
#     predictions = results["predictions"]
#     predictions = sorted(predictions, key=lambda item: item['x'])
#     symbols = [prediction["class"] for prediction in predictions]
#     return symbols
