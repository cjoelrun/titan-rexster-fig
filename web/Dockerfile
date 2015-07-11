FROM python:2.7

RUN mkdir -p /usr/src/web
WORKDIR /usr/src/web

COPY requirements.txt /usr/src/web/
RUN pip  install -v -r   requirements.txt

COPY . /usr/src/web
