FROM python:3.11-alpine3.17

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

RUN apk update && \
    apk add --no-cache gcc musl-dev postgresql-dev

RUN pip install --upgrade pip

COPY ./requirements.txt .

RUN pip install -r requirements.txt

WORKDIR /usr/src/app

COPY . .    

