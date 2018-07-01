FROM python:3.6.5

RUN apt-get update && apt-get install -y gettext

RUN mkdir -p /usrc/src/app
WORKDIR /usr/src/app

ENV PYTHONPATH=/usr/src/app

COPY setup.cfg .
COPY setup.py .
COPY README.rst .
COPY HISTORY.rst .
COPY rest_framework_recaptcha/__init__.py rest_framework_recaptcha/__init__.py

ARG target=.

RUN pip install -e "${target}"

COPY . .
