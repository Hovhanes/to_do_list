FROM python:3.7.8-buster
MAINTAINER Hovhannes Stepanyan

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/server

COPY ./ /usr/src/server

RUN cd /usr/src/server && pip install pipenv

RUN cd /usr/src/server && pipenv install --ignore-pipfile

COPY .infrastructure/docker/prod/bin/docker-entrypoint.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/docker-entrypoint.sh

ENTRYPOINT ["docker-entrypoint.sh"]