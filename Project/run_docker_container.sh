#!/bin/bash

echo "Starting docker container..."
docker-compose up -d

echo "Running db migrations..."
docker-compose exec electricity-provider python manage.py migrate
