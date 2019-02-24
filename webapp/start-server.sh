#!/usr/bin/env bash

PYTHONPATH=${PYTHONPATH}:../blog-generator FLASK_APP=putify.py pipenv run flask run
