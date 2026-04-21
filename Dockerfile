FROM python:3.11.4-alpine

WORKDIR /app

RUN pip install -i https://mirror-pypi.runflare.com/simple --upgrade pip

COPY . /app

RUN pip install -i https://mirror-pypi.runflare.com/simple -r requirements.txt
