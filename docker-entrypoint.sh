#!/bin/bash

export $(grep -v '^#' .env | xargs)
cd /app/src
python -u -m my_project

