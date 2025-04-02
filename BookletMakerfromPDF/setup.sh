#!/bin/bash

# Only run for *nix systems
# Check if Python is installed
if ! command -v python &> /dev/null
then
    echo "Python is not installed. Please install Python and try again."
    exit 1
fi

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install the required dependencies
pip install PyPDF2

# Make the bookl3t.py script executable
chmod +x bookl3t.py

echo "Setup complete. You can now run the bookl3t.py script."