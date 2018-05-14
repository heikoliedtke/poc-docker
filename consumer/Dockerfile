FROM python:alpine

WORKDIR /app

ADD . .


RUN pip install --no-cache-dir -r requirements.txt

CMD ["python3","consumer.py"]

