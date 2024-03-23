import cv2
import numpy as np
import requests

# Create a VideoCapture object and read from input file
# If the input is the camera, pass 0 instead of the video file name
VIDEO_PATH = "videos/test.mp4"
cap = cv2.VideoCapture(VIDEO_PATH)
# BASE_URL = "http://localhost:8000"
BASE_URL="https://accident-detector.proudcoast-e8949542.westus.azurecontainerapps.io"

# Read until video is completed

# Check if the video file opened successfully
if not cap.isOpened():
    print("Error: Could not open video.")
    exit()
frame_id = 0
# Read and display frame by frame
while True:
    # Read the next frame from the video
    ret, frame = cap.read()

    # Break the loop if there are no more frames
    if not ret:
        break

    _, buffer = cv2.imencode('.jpg', frame)
    io_buf = np.asarray(buffer, dtype=np.uint8).tobytes()

    # Display the frame
    request_url = f"{BASE_URL}/uploadframe/?frame_id={frame_id}"

    response = requests.post(
        request_url,
        files={"file": ("frame.jpg", io_buf, "image/jpeg")},
    )
    print(response.json())
    frame_id += 1

# Release the video capture object and close all frames
cap.release()
cv2.destroyAllWindows()
