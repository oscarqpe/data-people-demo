import logging
import os
import google.auth

from google.auth import impersonated_credentials
from google.auth.transport.requests import Request, AuthorizedSession
from google.oauth2.credentials import Credentials
from google.cloud import bigquery
from google.cloud import storage

SCOPES = [
    'https://www.googleapis.com/auth/ediscovery',
    'https://www.googleapis.com/auth/cloud-platform',
    'https://www.googleapis.com/auth/devstorage.full_control',
    'https://www.googleapis.com/auth/devstorage.read_write',
    'https://www.googleapis.com/auth/bigquery',
    'https://www.googleapis.com/auth/cloud-platform.read-only'
]
LIFETIME_TOKEN_IMPERSONATION = 300

def get_token_impersonated(email):
    credentials, project = google.auth.default()
    source_credentials = (credentials)
    target_credentials = impersonated_credentials.Credentials(
        source_credentials=source_credentials,
        target_principal=email,
        target_scopes=SCOPES,
        lifetime=LIFETIME_TOKEN_IMPERSONATION
    )
    credentials_token = Credentials(target_credentials.token)
    if (target_credentials.token is None) or credentials_token.expired:
        request = Request()
        target_credentials.refresh(request=request)
    success = True
    data = {
        'token': target_credentials.token
    }
    return data

def get_credential_impersonated(email):
    token = get_token_impersonated(email)
    credentials_token = Credentials(token=token.get("token"))
    return credentials_token

#credentials = service_account.Credentials.from_service_account_file(Constantes.SERVICE_ACCOUNT_FILE)

def query_bigquery(email):
    # Crear cliente de BigQuery
    client = bigquery.Client(credentials=get_credential_impersonated(email=email))

    # Definir la consulta SQL
    query = """
        SELECT *
        FROM `dev-apps-ikurana.data_people.persona`
        LIMIT 10
    """

    # Ejecutar la consulta
    query_job = client.query(query)

    # Recuperar y procesar los resultados
    results = query_job.result()  # Espera a que se complete la consulta

    # Iterar sobre los resultados y mostrar cada fila
    for row in results:
        print(row)

def download_blob(bucket_name, source_blob_name, destination_file_name, email):

    # Crear el cliente de Google Cloud Storage
    storage_client = storage.Client(credentials=get_credential_impersonated(email=email))

    # Obtener el bucket y el blob (archivo) que queremos descargar
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(source_blob_name)

    # Descargar el archivo
    blob.download_to_filename(destination_file_name)

    print(f"Archivo {source_blob_name} descargado a {destination_file_name}.")

SERVICE_ACCOUNT_1="test-sa-imp1-data-people@dev-apps-ikurana.iam.gserviceaccount.com"
SERVICE_ACCOUNT_2="test-sa-imp2-data-people@dev-apps-ikurana.iam.gserviceaccount.com"

# example 1
query_bigquery(SERVICE_ACCOUNT_1)

# example 2
BUCKET = "test-data-people-day6"
FILE = "pokemon.jpg"
DESTINATION = f"./download/{FILE}"
#download_blob(BUCKET, FILE, DESTINATION, SERVICE_ACCOUNT_2)