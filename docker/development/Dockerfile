FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY ./backend/requirements/development.txt /app/backend/requirements/

RUN pip install -r backend/requirements/development.txt
