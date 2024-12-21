FROM python:3.12-alpine3.17

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

RUN apk update && \
    apk add --no-cache gcc musl-dev postgresql-dev

RUN pip install --upgrade pip

WORKDIR /backend/django/manage.py

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["sh", "-c", "python django/manage.py makemigrations && python django/manage.py migrate && python django/manage.py runserver"]