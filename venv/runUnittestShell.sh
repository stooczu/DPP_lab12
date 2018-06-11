#!/usr/bin/env bash

echo $PWD

ls -l

python venv/run_test_module.py -o coverage.xml
##cp -r coverage.xml /var/lib/jenkins/workspace/DPP_lab12/coverage.xml
##cp -r ./python_unittests_xml /var/lib/jenkins/workspace/DPP_lab12/python_unittests_xml