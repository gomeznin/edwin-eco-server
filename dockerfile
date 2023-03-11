FROM python:3.9-slim-buster
RUN apt-get update && apt-get install -y netcat
COPY requirements.txt /app/
WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt
COPY edwin-eco-server.py /app/
CMD python edwin-eco-server.py

