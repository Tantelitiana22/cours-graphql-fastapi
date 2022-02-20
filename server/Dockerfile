FROM python:3.8-slim

WORKDIR /server

COPY Pipfile .
COPY extract-package.py .

RUN apt-get update \
    && apt-get install gcc -y \
    && apt-get clean

RUN pip install --upgrade pip
RUN pip install Pipfile
RUN python3 extract-package.py
RUN pip install -r requirements.txt\
    && rm -rf /root/.cache/pip

COPY . .
