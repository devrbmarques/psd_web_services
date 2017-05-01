#!/bin/bash
rm flaskr/salas.db
sudo pip install --editable .
export FLASK_APP=flaskr
clear
flask initdb
#flask run
