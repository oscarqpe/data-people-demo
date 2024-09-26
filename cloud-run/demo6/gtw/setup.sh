PROJECT_ID=dev-apps-ikurana
API_ID=api-gtw-test
API_ID_HASH=

echo ""
echo "--- CREATE API ---"
echo ""
# gcloud beta api-gateway apis create api-gtw-test --project=dev-apps-ikurana

gcloud beta api-gateway apis create $API_ID --project=$PROJECT_ID

#gcloud api-gateway apis describe api-gtw-test --location=us-central1 --format="get(defaultHostname)"


gcloud beta api-gateway api-configs create config-test \
  --api=api-gtw-test --openapi-spec=api.yaml \
  --project=dev-apps-ikurana --backend-auth-service-account=test-sa-data-people@dev-apps-ikurana.iam.gserviceaccount.com

echo ""
echo "--- ENABLE API ---"
echo ""
echo "API_ID_HASH=$API_ID_HASH"

echo ""
gcloud services enable $(gcloud api-gateway apis describe api-gtw-test --format="get(managedService)")


echo ""
echo "--- CREATE A GATEWAY ---"
echo "---"
echo ""

gcloud beta api-gateway gateways create gateway-test \
  --api=api-gtw-test --api-config=config-test \
  --location=us-central1 --project=dev-apps-ikurana

echo ""
echo "-- DESCRIBE GATEWAY ---"
echo ""

gcloud beta api-gateway gateways describe gateway-test \
  --location=us-central1 --project=dev-apps-ikurana