#!/bin/bash

IDENTITY_TOKEN=$(gcloud auth print-identity-token)

curl -H "Authorization: Bearer "$IDENTITY_TOKEN https://hello-world-4-rjjdx7lt6q-uc.a.run.app 