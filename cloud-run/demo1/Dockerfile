# Usa la imagen base de Python 3.11 sobre Alpine Linux
FROM python:3.11-alpine

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos de dependencias a la imagen
COPY requirements.txt requirements.txt

# Instala las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia el código de la aplicación a la imagen
COPY . .

# Expone el puerto 8080 (requerido por Cloud Run)
EXPOSE 8080

# Comando para ejecutar la aplicación Flask
CMD ["python", "app.py"]
