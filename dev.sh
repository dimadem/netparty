#! /bin/bash

source .venv/bin/activate
export PYTHONPATH="${PYTHONPATH}:$(pwd)"
python3 ./app/main.py