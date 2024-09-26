import base64
import json
from flask import Flask, request, jsonify, render_template, redirect, url_for
import firebase_admin
from firebase_admin import credentials, auth
import jwt
import logging
logger = logging.getLogger(__name__)
# Inicializar la app de Firebase
#cred = credentials.Certificate("firebase_admin_credentials.json")
firebase_admin.initialize_app()

app = Flask(__name__, template_folder="templates")

def base64decode(string_decode):
    try:
        string_bytes = base64.urlsafe_b64decode(string_decode)
    except Exception as e:
        string_bytes = base64.b64decode(string_decode)
    return string_bytes

# Ruta principal para mostrar el formulario de login
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para verificar el token de Firebase
@app.route('/verify_token', methods=['POST'])
def verify_token():
    if 'Authorization' in request.headers:
        token = request.headers['Authorization']
        logger.exception("Token Local")
        logger.exception(token)
    if 'X-Apigateway-Api-Userinfo' in request.headers:
        user_info = request.headers['X-Apigateway-Api-Userinfo']
        logger.exception("Token Gateway")
        logger.exception(user_info)

    try:
        # Verificar el token con Firebase Admin SDK
        json_user_info = json.loads(base64decode(user_info + "=="))
        email = json_user_info.get("email")
        return jsonify({'message': 'Token válido', 'email': email})

    except Exception as e:
        logger.exception(e)
        return jsonify({'error': str(e)}), 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
