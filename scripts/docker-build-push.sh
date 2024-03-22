#!/bin/bash
VERSION=latest

#az login
az acr login --name detector

docker build -t detector.azurecr.io/detector:$VERSION .
docker push detector.azurecr.io/detector:$VERSION
