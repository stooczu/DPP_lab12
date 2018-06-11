#!/usr/bin/env bash
set -e

virtualenv venv --distribute -p python

PYTHONPATH=. venv run_test_module.py
PYTHONPATH=. venv report --omit=venv/*
PYTHONPATH=. venv html --omit=venv/*
PYTHONPATH=. venv xml --omit=venv/*