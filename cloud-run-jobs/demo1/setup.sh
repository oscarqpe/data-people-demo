#!/bin/bash

PROJECT_ID="dev-apps-ikurana"
REGION="us-central1"
SERVICE_ACCOUNT="test-sa-data-people@dev-apps-ikurana.iam.gserviceaccount.com"
RUN_JOB="hello-job-1"

gcloud config set project $PROJECT_ID

gcloud builds submit --tag gcr.io/$PROJECT_ID/$RUN_JOB

gcloud run jobs $1 ${RUN_JOB} \
  --image gcr.io/$PROJECT_ID/${RUN_JOB}\
  --tasks 2 \
  --set-env-vars SLEEP_MS=10000 \
  --set-env-vars FAIL_RATE=0.5 \
  --cpu=1 \
  --memory=1Gi \
  --max-retries 2 \
  --region $REGION \
  --project=$PROJECT_ID \
  --service-account $SERVICE_ACCOUNT \
  --task-timeout 60m

# --parallelism [# de tareas]