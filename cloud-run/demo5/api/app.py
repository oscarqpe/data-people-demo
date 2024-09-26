from flask import Flask, request, jsonify, render_template, redirect, url_for
import firebase_admin
from firebase_admin import credentials, auth
import jwt

# Inicializar la app de Firebase
#cred = credentials.Certificate("firebase_admin_credentials.json")
firebase_admin.initialize_app()

app = Flask(__name__, template_folder="templates")

# Ruta principal para mostrar el formulario de login
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para verificar el token de Firebase
@app.route('/verify_token', methods=['POST'])
def verify_token():
    id_token = request.json.get('id_token')

    if not id_token:
        return jsonify({'error': 'Token no proporcionado'}), 400

    try:
        # Verificar el token con Firebase Admin SDK
        decoded_token = auth.verify_id_token(id_token)
        uid = decoded_token['uid']
        email = decoded_token.get('email')
        return jsonify({'message': 'Token válido', 'uid': uid, 'email': email})

    except Exception as e:
        return jsonify({'error': str(e)}), 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
