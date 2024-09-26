#!/bin/bash

PROJECT_ID="dev-apps-ikurana"
REGION="us-central1"
SERVICE_ACCOUNT="test-sa-data-people@dev-apps-ikurana.iam.gserviceaccount.com"
RUN_SERVICE="hello-world-1"

gcloud config set project $PROJECT_ID

gcloud builds submit --tag gcr.io/$PROJECT_ID/$RUN_SERVICE

gcloud run deploy $RUN_SERVICE \
  --image gcr.io/$PROJECT_ID/$RUN_SERVICE \
  --platform managed \
  --region $REGION \
  --allow-unauthenticated \
  --concurrency=1
