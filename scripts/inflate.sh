#!/bin/bash

DIR="$(cd "$(dirname "$0")" && pwd)"
cd $DIR/..

PYTHON_VERSION="3.10.4"
pyenv install --skip-existing $PYTHON_VERSION
pyenv local $PYTHON_VERSION
pyenv uninstall -f park_wait_times
pyenv virtualenv $PYTHON_VERSION park_wait_times
pyenv local park_wait_times

pip install --upgrade pip
pip install wheel
pip install -r requirements.txt

pyenv rehash

pre-commit install
