#!/bin/sh
# check health of database before making it available

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

python manage.py migrate --fake quizzes zero
python manage.py flush --no-input # removes all data from database
python manage.py makemigrations
python manage.py migrate --no-input
python manage.py collectstatic --no-input --clear # collects static files into STATIC_ROOT
python manage.py loaddata data.json

exec "$@"
