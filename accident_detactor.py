# from license_plate_detactor import detact_license_plate, extract_license_plate_symbols
# import cv2
# from server.utils import crop_frame_by_detaction
# import os
# from roboflow_client import ROBOFLOW_CLIENT as ROBOFLOW_CLIENT
# from make_call import make_call
#
# VIDEO_PATH = "videos/accident1.mp4"
# IMAGE_OUTPUT_DIR = "output"
# SYMBOLS_IN_LIST = set()
# for frame_id, frame, results in ROBOFLOW_CLIENT.infer_on_stream(VIDEO_PATH, model_id="incidents-project/1"):
#     for prediction in results["predictions"]:
#         if prediction["class"] != "vehicle":
#             continue
#         accident_crop_res = crop_frame_by_detaction(frame, prediction)
#         if accident_crop_res is not None:
#             cropped_license_plate_res_ = detact_license_plate(frame)
#             if cropped_license_plate_res_ is not None:
#                 cropped_license_plate_frame, *_ = cropped_license_plate_res_
#                 symbols = extract_license_plate_symbols(cropped_license_plate_frame)
#                 symbols_string = ' '.join(symbols)
#                 if symbols_string in SYMBOLS_IN_LIST or (len(symbols) != 7 and len(symbols) != 8):
#                     continue
#                 SYMBOLS_IN_LIST.add(symbols_string)
#                 print(symbols_string)
#                 output_path = os.path.join(IMAGE_OUTPUT_DIR, str(frame_id))
#                 os.makedirs(output_path, exist_ok=True)
#                 cv2.imwrite(os.path.join(output_path, "crash.jpg"), frame)
#                 cv2.imwrite(os.path.join(output_path, "cropped_license_plate.jpg"), cropped_license_plate_frame)
#
# make_call(SYMBOLS_IN_LIST)