# Python resmi imajını temel alıyoruz
FROM python:3.10

# Çalışma dizinini ayarlıyoruz
WORKDIR /app

COPY requirements.txt requirements.txt
COPY conservationServer.py conservationServer.py

# Gerekli bağımlılıkları yüklüyoruz
RUN pip install --no-cache-dir -r requirements.txt

# Expose port
ARG FLASK_PORT
ENV FLASK_PORT=${FLASK_PORT}
EXPOSE ${FLASK_PORT}

# Flask sunucusunu çalıştırma komutu
CMD ["python3", "conservationServer.py"]
