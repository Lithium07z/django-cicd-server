#!/bin/bash
REPOSITORY=/home/ubuntu

cd $REPOSITORY/django-cicd-server
echo "down docker compose : ubuntu"
sudo docker down

#docker compose release
echo "start docker compose up : ubuntu"
sudo docker compose -f /home/ubuntu/django-cicd-server/docker-compose.yml up --build -d