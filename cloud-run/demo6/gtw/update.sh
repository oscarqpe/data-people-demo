VERSION=$(date '+%Y-%m-%d-%H-%M-%S')
#echo $VERSION > version.sh
REGION='us-central1'
API_ID='api-gtw-test'
CONFIG_ID="config-api-${VERSION}"
PROJECT_ID='dev-apps-ikurana'
SERVICE_ACCOUNT_GTW='test-sa-data-people@dev-apps-ikurana.iam.gserviceaccount.com'
GATEWAY_ID='gateway-test'

echo ""
echo "--- CREATE API CONFIG (VERSION:$VERSION)---"
echo ""
gcloud beta api-gateway api-configs create $CONFIG_ID \
    --api=$API_ID --openapi-spec=api.yaml \
    --project=$PROJECT_ID --backend-auth-service-account=$SERVICE_ACCOUNT_GTW

echo ""
echo "--- UPDATE A GATEWAY ---"
echo "---"
echo ""

gcloud beta api-gateway gateways update $GATEWAY_ID \
    --api=$API_ID --api-config=$CONFIG_ID \
    --location=$REGION --project=$PROJECT_ID