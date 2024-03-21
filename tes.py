import requests

licece_list = ["1234567", "1234568", "1234569"]
BASE_URL = "http://localhost:8000/report_accident/"
payload = {"license_plates": licece_list}

res = requests.post(BASE_URL, json=licece_list)
