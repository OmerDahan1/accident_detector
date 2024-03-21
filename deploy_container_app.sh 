#!/bin/bash

# Define variables
ACR_NAME="${{ vars.REPOSITORY_NAME }}"
CONTAINER_APP_NAME="accident-detector"
RESOURCE_GROUP="accident-detection"
IMAGE_TO_DEPLOY="${{ secrets.REGISTRY_LOGIN_SERVER }}/${{ vars.REPOSITORY_NAME }}:${{ github.ref_name }}-${{ github.run_number }}"

# Login to Azure Container Registry
echo "Logging in to Azure Container Registry..."
az acr login --name $ACR_NAME

# Deploy the container image to Azure Container App
echo "Deploying container app..."
az containerapp update \
  --name $CONTAINER_APP_NAME \
  --resource-group $RESOURCE_GROUP \
  --image $IMAGE_TO_DEPLOY \
  --environment-variables ROBOFLOW_API_KEY="${{ secrets.ROBOFLOW_API_KEY }}" CALLER_API_KEY="${{ secrets.CALLER_API_KEY }}" CALLER_SECRET_KEY="${{ secrets.CALLER_SECRET_KEY }}"

echo "Deployment completed successfully."

# Note: Make sure to replace the variable placeholders with the actual values where necessary.
