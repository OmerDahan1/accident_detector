from fastapi import FastAPI, File, UploadFile, BackgroundTasks
from fastapi.responses import JSONResponse
import cv2
import numpy as np
from .accident_detactor import AccidentDetector
from .caller import make_call

app = FastAPI()
accident_detector = AccidentDetector()


@app.post("/uploadframe/")
async def upload_frame(background_tasks: BackgroundTasks, frame_id: int, file: UploadFile = File(...)):
    contents = await file.read()
    nparr = np.frombuffer(contents, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    background_tasks.add_task(process_image, img, frame_id)
    return {"message": f"Processing the {frame_id} in the background"}


@app.get("/get_license_plate_symbols/")
async def get_license_plate_symbols():
    return JSONResponse(content=accident_detector.symbols_list)


@app.post("/report_accident/")
async def report_accident(plates: list[str]):
    make_call(plates)
    accident_detector.symbols_list = []
    return {"message": f"Calling the emergency service for the following cars: {plates}"}


def process_image(image, frame_id):
    return accident_detector.detact(image, frame_id)
