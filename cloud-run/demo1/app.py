# app.py
import time
from flask import Flask

app = Flask(__name__)
start_time = time.time()

@app.route('/')
def hello_world():
    cold_start_duration = time.time() - start_time
    return f'Hola Mundo desde Flask en Cloud Run\nStart duration: {cold_start_duration:.2f} seconds'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
