import os
import requests

key = "e6caa3ae-3e08-4fd7-9ee5-40fa4756e26d"
secret = os.environ.get("SINCH_SECRET_KEY")

def get_call_text(lisence_plate_number_list):
  text = f"i am calling from the car accident detection system. We have a car accident at Haifa."
  if (lisence_plate_number_list is not None):
    text += "The following cars with lisence plate number has detected:"
    for lisence_plate_number in lisence_plate_number_list:
      text += f"lisence number  {lisence_plate_number}."

  text += "Please hurry up and come here as soon as possible. Thank you."
  return text

def make_call(lisence_plate_number_list):
  from_number = "+447520662233"
  to = "+9720543155331"
  locale = "en-US"
  url = "https://calling.api.sinch.com/calling/v1/callouts"

  payload = {
    "method": "ttsCallout",
    "ttsCallout": {
      "cli": from_number,
      "destination": {
        "type": "number",
        "endpoint": to
      },
      "locale": locale,
      "text": get_call_text(lisence_plate_number_list)
    }
  }
  headers = {"Content-Type": "application/json"}

  response = requests.post(url, json=payload, headers=headers, auth=(key, secret))

  data = response.json()
  print(data)


