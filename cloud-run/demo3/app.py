# app.py
import time
from flask import Flask
import pandas as pd

app = Flask(__name__)
start_time = time.time()

@app.route('/')
def hello_world():
    # Crear un pequeño DataFrame de ejemplo con Pandas
    cold_start_duration = time.time() - start_time
    df = pd.DataFrame({
        'Nombre': ['Alice', 'Bob', 'Charlie'],
        'Edad': [25, 30, 35]
    })
    return f'Hola Mundo desde Flask en Cloud Run con Pandas\n\n{df.to_string()}\nStart duration: {cold_start_duration:.2f} seconds'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
