#!/bin/bash
# permissions:
# test-sa-data-people@dev-apps-ikurana.iam.gserviceaccount.com
# - storage object admin
# - cloud function developer

PROJECT_ID="dev-apps-ikurana"
REGION="us-central1"
SERVICE_ACCOUNT="test-sa-data-people@dev-apps-ikurana.iam.gserviceaccount.com"
BUCKET="test-data-people-day6"
FUNCTION_NAME="generateThumbnail"
ENTRE_POINT="generateThumbnail"

gcloud config set project $PROJECT_ID

gcloud functions deploy $FUNCTION_NAME \
  --no-gen2 \
  --runtime nodejs20 \
  --trigger-resource $BUCKET \
  --trigger-event google.storage.object.finalize \
  --entry-point $ENTRE_POINT \
  --region $REGION
  --memory 512MB \
  --timeout 60s \
  --service-account $SERVICE_ACCOUNT
