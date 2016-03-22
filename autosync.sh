#!/bin/bash
set -e

rm db.sqlite3 | true ;

find . -name '*.pyc' -delete
rm -fr media/*
rm -fr logs/*
rm -fr project/**/migrations/*.py

python manage.py makemigrations --noinput
python manage.py makemigrations app
python manage.py migrate --noinput
if [ "$1" != "--empty" ]; then
    python manage.py datacreator
fi

touch project/settings.py
