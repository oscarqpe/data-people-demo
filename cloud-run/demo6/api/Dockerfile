# Usa una imagen base de Python
FROM python:3.11-alpine

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar los archivos al contenedor
COPY . /app/

# Instalar dependencias
RUN pip install -r requirements.txt

# Exponer el puerto 8080 para Cloud Run
EXPOSE 8080

# Ejecutar la aplicación
CMD ["python", "app.py"]
