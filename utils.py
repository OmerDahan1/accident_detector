import math


def crop_frame_by_detaction(frame, prediction) -> (object, int, int, int, int):
    """

    :param frame:
    :param detection:
    :return: object, x1, y1, x2, y2
    """
    roi_x = int(prediction['x'] - prediction['width'] / 2)
    roi_y = int(prediction['y'] - prediction['height'] / 2)
    roi_width = int(prediction['width'])
    roi_height = int(prediction['height'])
    roi = frame[roi_y:roi_y + roi_height, roi_x:roi_x + roi_width]

    return roi, roi_x, roi_y, roi_x + roi_width, roi_y + roi_height

def sort_prediction(predictions):
    return sorted(predictions, key=lambda item: item['x'])