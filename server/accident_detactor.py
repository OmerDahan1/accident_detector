from .license_plate_detactor import LicensePlateDetector
from .utils import crop_frame_by_detaction
from server import CLIENT


class AccidentDetector:
    def __init__(self):
        self.symbols_list = []
        self.counter = 0
        self.license_plate_detector = LicensePlateDetector()

    def detact(self, frame):
        try:
            results = CLIENT.infer(frame, model_id="incidents-project/1")
        except Exception as e:
            print(f"An error occurred during the external API call: {e}")
            # Optionally log the error or handle it as needed
            return None  # or handle it in another appropriate way

        for prediction in results["predictions"]:
            if prediction["class"] != "vehicle":
                continue

            accident_crop_res = crop_frame_by_detaction(frame, prediction)
            if accident_crop_res is not None:
                cropped_license_plate_res_ = self.license_plate_detector.detact(frame)
                if cropped_license_plate_res_ is not None:
                    cropped_license_plate_frame, *_ = cropped_license_plate_res_
                    symbols = self.license_plate_detector.extract_license_plate_symbols(cropped_license_plate_frame)
                    symbols_string = ' '.join(symbols)
                    if symbols_string in self.symbols_list or (len(symbols) != 7 and len(symbols) != 8):
                        continue
                    print(f"added {symbols_string}")
                    self.symbols_list.append(symbols_string)

        # Depending on your application's needs, you might want to return some information even when the API fails
        return None  # or return a meaningful value
