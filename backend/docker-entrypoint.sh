#!/bin/sh
set -e
until cd /menu-manager-API
do
    echo "Wait for server volume..."
done


until python manage.py migrate
do
    echo "Waiting for postgres ready..."
done

python manage.py collectstatic

gunicorn menu_manager.wsgi:application --bind 8000 --workers 4 --threads 4
