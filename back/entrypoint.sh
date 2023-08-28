#!/bin/ash

echo "Apply database Migrations "
python manage.py migrate

exec "$@"