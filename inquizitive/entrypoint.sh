#!/bin/sh

#checks whether postgres is healthy and applies migrations before running dev server

if [ "$DATABASE" = "postgres" ] 
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

python manage.py flush --no-input
python manage.py migrate
python manage.py makemigrations
python manage.py loaddata data.json
python manage.py loaddata user-data.json

exec "$@"
