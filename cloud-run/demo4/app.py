from flask import Flask, request
import jwt
import logging

logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.route('/')
def hello_world():
    for key in request.headers.keys():
        logger.exception(f"{key} {request.headers.get(key)}")
    auth_header = request.headers.get('Authorization', None)
    logger.exception("Authorization: " + auth_header)
    if not auth_header or not (auth_header.startswith('Bearer ') or auth_header.startswith('bearer ')):
        return {'error': 'No se proporcionó un token válido'}, 401
    
    id_info = jwt.decode(auth_header.split(" ")[1], options={"verify_signature": False})
    return id_info

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
