FROM python:3.13.0-slim-bullseye
RUN apt-get -y update; apt-get -y install curl
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY app.py .
ENTRYPOINT ["python", "app.py"]
