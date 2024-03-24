# Accident Detactor
## About
This API employs advanced computer vision and deep learning technologies to automatically detect car accidents in real-time and immediately alert emergency services. Built with Python, it leverages sophisticated AI models for precise incident recognition and extracts vital information, such as license plate numbers. To expose this functionality efficiently, we utilize FASTAPI, a modern, fast (high-performance) web framework for building APIs with Python 3.10+ that significantly simplifies the development process and allows for easy integration and scalability. This system aims to drastically reduce emergency response times by providing accurate, instantaneous data on accidents, enhancing road safety, and potentially saving lives. The integration of FASTAPI ensures our project is at the forefront of emergency response technology, offering a robust and scalable solution for public safety advancements.

## Local Setup
### Requirements

1. Install dependencies
```
pip install -r requirements.txt
```
2.  set the environment variables
Get your API keys from
[SINCH](https://www.sinch.com/)  and
[ROBOFLOW](https://universe.roboflow.com/)

```
ROBOFLOW_API_KEY=your_api_key
CALLER_API_KEY="sinch_api_key"
CALLER_SECRET_KEY="sinch_secret_key"
DEPLOYMENT=local
```



## Usage
###  Create a video feed to the server
1. place your video file in `videos` folder with the name `test.mp4`
2. ```python video_streamer.py``` to start the video feed
3. ```python emergency_service.py``` to check for accidents in the video feed





