import math
from license_plate_detactor import detact_license_plate,extract_license_plate_symbols
import cv2
from utils import crop_frame_by_detaction
import os
from roboflow_client import CLIENT as CLIENT
from collections import deque

VIDEO_PATH = "omer-crash.mp4"
IMAGE_OUTPUT_DIR = "output"
BUFFER_SECONDS = 5
FPS = 30
BUFFER_SIZE = FPS * BUFFER_SECONDS  # Adjust based on your needs (e.g., 30 frames for 1 second at 30 FPS)
frame_buffer = deque(maxlen=BUFFER_SIZE)

for frame_id, frame, results in CLIENT.infer_on_stream(VIDEO_PATH, model_id="incidents-project/1"):
    frame_buffer.append((frame_id, frame))  # Update the buffer with the latest frame
    for buffered_frame_id, buffered_frame in frame_buffer:
        for prediction in results["predictions"]:
            if prediction["class"] != "vehicle":
                continue
            accident_crop_res = crop_frame_by_detaction(frame, prediction)
            if accident_crop_res is not None:
                # cropped_crash_frame, *_ = accident_crop_res
                cropped_license_plate_res_ = detact_license_plate(frame)
                sybol = extract_license_plate_symbols(frame)
                if cropped_license_plate_res_ is not None:
                    cropped_license_plate_frame, *_ = cropped_license_plate_res_
                    output_path = os.path.join(IMAGE_OUTPUT_DIR, str(buffered_frame_id))
                    os.makedirs(output_path, exist_ok=True)
                    cv2.imwrite(os.path.join(output_path, "crash.jpg"), buffered_frame)
                    # cv2.imwrite(os.path.join(output_path, "cropped_crash_frame.jpg"), cropped_crash_frame)
                    cv2.imwrite(os.path.join(output_path, "cropped_license_plate.jpg"), cropped_license_plate_frame)
