#!/bin/bash

# Run the setup script
source setup.bash

# Run the Flask app in the background
(cd src && pip install -r requirements.txt && python flask_app.py &) 

# Run the Raspberry Pi script in the background
python main.py &
