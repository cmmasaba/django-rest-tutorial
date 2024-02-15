FROM python:3.12

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /tutorial

COPY Pipfile Pipfile.lock /tutorial/
RUN pip install pipenv && pipenv install --system

COPY . /tutorial/