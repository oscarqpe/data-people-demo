#!/bin/bash
# permissions:
# SA: test-sa-data-people@dev-apps-ikurana.iam.gserviceaccount.com
# - storage object admin
# - cloud function developer
# - eventarc admin
# SA: service-[NUMBER-PROJECT]@gs-project-accounts.iam.gserviceaccount.com
# - pub/sub publisher 

PROJECT_ID="dev-apps-ikurana"
REGION="us-central1"
SERVICE_ACCOUNT="test-sa-data-people@dev-apps-ikurana.iam.gserviceaccount.com"
BUCKET="test-data-people-day6-2"
FUNCTION_NAME="generateThumbnail2"
ENTRE_POINT="generateThumbnail2"

gcloud functions deploy $FUNCTION_NAME \
  --gen2 \
  --runtime nodejs20 \
  --trigger-resource $BUCKET \
  --trigger-event google.storage.object.finalize \
  --region $REGION \
  --entry-point $ENTRE_POINT \
  --memory 1GB \
  --cpu 2 \
  --source . \
  --service-account $SERVICE_ACCOUNT