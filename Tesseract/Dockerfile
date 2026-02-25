FROM python:3.11-slim-bullseye

RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    tesseract-ocr-eng \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
    
RUN pip install flask pytesseract pillow

WORKDIR /app
COPY app.py .

EXPOSE 5000
CMD ["python" , "app.py"]