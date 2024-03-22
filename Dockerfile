#
FROM python:3.10

#
WORKDIR /code

#
COPY ./requirements.txt /code/requirements.txt

#
RUN apt-get update && apt-get install -y libgl1-mesa-glx

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

#
COPY ./server /code/server

#
CMD ["uvicorn", "server.main:app", "--host", "0.0.0.0", "--port", "80"]