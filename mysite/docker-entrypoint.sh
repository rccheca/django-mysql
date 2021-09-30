#!/bin/bash

#wait for it
#./wait.sh -h mysql -p 3306
sleep 30

# Collect static files
echo "Collect static files"
python manage.py collectstatic --noinput

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate

# Start server
echo "Starting server"
python manage.py runserver 0.0.0.0:$PORT