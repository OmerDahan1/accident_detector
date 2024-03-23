from .license_plate_detactor import LicensePlateDetector
from .utils import crop_frame_by_detaction
from server import ROBOFLOW_CLIENT
from server import logger


class AccidentDetector:
    def __init__(self):
        self.symbols_list = []
        self.counter = 0
        self.license_plate_detector = LicensePlateDetector()

    def detact(self, frame, frame_id):
        symbols_string = ""
        logger.info(f"Processing frame {frame_id} in the background")
        try:
            results = ROBOFLOW_CLIENT.infer(frame, model_id="incidents-project/1")
        except Exception as e:
            logger.exception(f"An error occurred during the external API call: {e}")
            return None  # or handle it in another appropriate way

        # logger.info(f"frame {frame_id}: {results}")
        for prediction in results["predictions"]:

            # if prediction["class"] != "severe" or prediction["class"] != "moderate":
            if prediction["class"] != "vehicle":
                # logger.info(f"frame {frame_id}: no predictions")
                continue
            # logger.info(f"frame {frame_id}: detacted accident in - class {prediction['class']}")
            accident_crop_res = crop_frame_by_detaction(frame, prediction)
            if accident_crop_res is not None:
                cropped_license_plate_res_ = self.license_plate_detector.detact(frame)
                if cropped_license_plate_res_ is not None:
                    cropped_license_plate_frame, *_ = cropped_license_plate_res_
                    symbols = self.license_plate_detector.extract_license_plate_symbols(cropped_license_plate_frame)
                    symbols_string = ' '.join(symbols)
                    if (len(symbols) != 7 and len(symbols) != 8):
                        logger.info(f"frame {frame_id}: license plate number is not valid ")
                        continue
                    if symbols_string in self.symbols_list:
                        logger.info(
                            f"frame {frame_id}: license plate {symbols_string} number is already in the list")
                        continue
                    logger.info(f"frame {frame_id}: added {symbols_string}")
                    self.symbols_list.append(symbols_string)

        # Depending on your application's needs, you might want to return some information even when the API fails
        return None  # or return a meaningful value
