import time
import os
import requests

BASE_URL = "http://localhost:8000"
# BASE_URL="https://accident-detector.proudcoast-e8949542.westus.azurecontainerapps.io"

if os.environ.get('DEPLOYMENT') == 'local':
    BASE_URL = "http://localhost:8000"
    print("running locally")
else:
    BASE_URL = "https://accident-detector.proudcoast-e8949542.westus.azurecontainerapps.io"
    print("running on azure")


def make_call(lisence_plate_number_list):
    request_url = f"{BASE_URL}/report_accident/"
    response = requests.post(request_url, json=lisence_plate_number_list)
    print(response.json())


def evalaute_status():
    request_url = f"{BASE_URL}/get_license_plate_symbols/"
    made_call = False
    while not made_call:
        licence_plates = requests.get(request_url)
        licence_plates = licence_plates.json()
        print(licence_plates)
        if len(licence_plates) > 0:
            print(f"Calling the emergency service for the following cars: {licence_plates}")
            make_call(licence_plates)
            made_call = True
        time.sleep(5)


evalaute_status()
