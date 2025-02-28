#!/bin/bash

# Set up environment variables
export PYTHONPATH="${PYTHONPATH}:$(pwd)/.."
unset PYTHONHOME

# Create and activate virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    /usr/bin/python3 -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Install requirements
echo "Installing requirements..."
pip install -r ../requirements.txt

# Run tests
echo "Running tests..."
python run_tests.py

# Deactivate virtual environment
deactivate 