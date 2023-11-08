#!/bin/bash

# Update the package list
sudo apt-get update

# Install sakis3g
sudo apt-get install sakis3g

# Install Python and pip
sudo apt-get install python3 python3-pip


# Install Python dependencies from requirements.txt
pip3 install -r requirements.txt

echo "Setup complete."
