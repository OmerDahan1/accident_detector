#!/bin/sh
docker build -t myimage .
docker run -p 8000:80 --env-file config.env myimage