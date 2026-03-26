FROM python:3.11-slim

# Carpeta de trabajo (no es donde estarán los archivos estáticos)
WORKDIR /app

# Ejecutamos un servidor HTTP simple que servirá archivos desde /data
CMD ["python", "-m", "http.server", "8000", "--directory", "/data"]