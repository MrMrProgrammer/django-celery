FROM python:3.11.4-alpine

WORKDIR /app

RUN pip install -i https://mirror2.chabokan.net/pypi/simple --upgrade pip

COPY . /app

RUN pip install -i https://mirror2.chabokan.net/pypi/simple -r requirements.txt
