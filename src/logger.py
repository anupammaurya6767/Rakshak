import logging

# Configure logging
log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
logging.basicConfig(filename="data/logs/security.log", level=logging.INFO, format=log_format)

# Create a logger for the entire project
logger = logging.getLogger("security_project")
