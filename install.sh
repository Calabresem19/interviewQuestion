#!/bin/bash


sudo apt-get install python-pip
sudo pip install flask
sudo pip install requests
sudo pip install geopy
sudo pip install mysql-connector

export FLASK_APP=server.py
