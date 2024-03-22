#!/bin/bash

# Define variables
ACR_NAME="$REPOSITORY_NAME"
CONTAINER_APP_NAME="accident-detector"
RESOURCE_GROUP="accident-detection"
IMAGE_TO_DEPLOY="$REGISTRY_LOGIN_SERVER/$REPOSITORY_NAME:${GITHUB_REF_NAME}-${GITHUB_RUN_NUMBER}"

# Login to Azure Container Registry
echo "Logging in to Azure Container Registry..."
az acr login --name $ACR_NAME

# Deploy the container image to Azure Container App
echo "Deploying container app..."
az containerapp update \
  --name $CONTAINER_APP_NAME \
  --resource-group $RESOURCE_GROUP \
  --image $IMAGE_TO_DEPLOY \
  --environment-variables ROBOFLOW_API_KEY="$ROBOFLOW_API_KEY" CALLER_API_KEY="$CALLER_API_KEY" CALLER_SECRET_KEY="$CALLER_SECRET_KEY"

echo "Deployment completed successfully."
