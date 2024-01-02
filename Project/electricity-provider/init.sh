#!/bin/sh

sleep 15
# Start the server in the background
python3 manage.py runserver 0.0.0.0:8000 &

# Perform the migration
python3 manage.py migrate

# Wait for the server process to finish
wait %1
