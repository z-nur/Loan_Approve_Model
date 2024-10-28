# Python 3.9 slim tabanlı bir Docker imajı 
FROM python:3.9-slim

# Çalışma dizini
WORKDIR /app

# Gerekli dosyaları Docker imajına kopyalayın
COPY . /app

# Gereksinimler
RUN pip install --no-cache-dir -r requirements.txt

# API için port
EXPOSE 5001

# Flask uygulaması
CMD ["python", "app.py"]
