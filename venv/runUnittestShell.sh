#!/usr/bin/env bash
set -e

virtualenv venv --distribute -p python
source venv

pip install -r requirements.txt
PYTHONPATH=. venv/bin/coverage run run_test_module.py
PYTHONPATH=. venv/bin/coverage report --omit=venv/*
PYTHONPATH=. venv/bin/coverage html --omit=venv/*
PYTHONPATH=. venv/bin/coverage xml --omit=venv/*