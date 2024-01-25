# autollm/utils/logging.py

import logging

# Logger configuration for read_files_as_documents function
import logging

# Configure the logger
read_files_logger = logging.getLogger('autollm.read_files')
read_files_logger.setLevel(logging.INFO)

# Create a console handler with a specific format
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)

# Add the handler to the logger
read_files_logger.addHandler(ch)

# Ensure that log messages propagate up to the root logger
logger = logging.getLogger('autollm')
logger.setLevel(logging.INFO)

# Create a console handler with a specific format
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)

# Add the handler to the logger
logger.addHandler(ch)

# Ensure that log messages propagate up to the root logger
logger.propagate = False
