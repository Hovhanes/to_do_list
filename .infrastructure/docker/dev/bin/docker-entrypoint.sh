#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

echo "Starting migrate"
pipenv run python manage.py flush --no-input
pipenv run python manage.py migrate
echo "Starting tests"
pipenv run python manage.py test

exec "$@"