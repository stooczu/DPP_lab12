#!/usr/bin/env bash
set -e

virtualenv venv --distribute -p python

pip install -r xmlrunner==1.7.7
pip install -r coverage==5.0a1
PYTHONPATH=. venv run_test_module.py
PYTHONPATH=. venv report --omit=venv/*
PYTHONPATH=. venv html --omit=venv/*
PYTHONPATH=. venv xml --omit=venv/*