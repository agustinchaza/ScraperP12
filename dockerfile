# Usa una imagen base con Python
FROM python:3.10

# Configura el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos del proyecto al contenedor
COPY . /app

# Instala las dependencias, incluyendo Twisted 22.10.0
RUN pip install --no-cache-dir -r requirements.txt

# Define el directorio de Scrapy (cambia esto si es diferente)
WORKDIR /app/scrapy

# Comando por defecto (se puede sobreescribir en run)
CMD ["scrapy", "crawl", "pagina12", "-o", "output.csv"]
