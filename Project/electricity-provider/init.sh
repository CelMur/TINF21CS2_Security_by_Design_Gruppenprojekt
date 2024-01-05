#!/bin/sh
echo "Waiting for postgres..."
sleep 15
echo "Trying to run server..."
# Start the server in the background
python3 manage.py runserver 0.0.0.0:8000 &
# Perform the migration
python3 manage.py migrate
# initialize the database with data
python3 manage.py create_initial_energy_tariffs
# Wait for the server process to finish
wait %1