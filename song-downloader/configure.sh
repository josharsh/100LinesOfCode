#!/bin/bash

echo "Creating a virutal env..."
python3 -m venv venv

. venv/bin/activate

echo "Installing dependencies..."
pip install -r requirements.txt
