import logging
import sys

logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)

def handle_exception(exc_type, exc_value, exc_traceback):
    """
    Handle exceptions by logging the exception message and traceback.
    """
    logger.error("Exception occurred:", exc_info=(exc_type, exc_value, exc_traceback))

def handle_error(error_message):
    """
    Handle errors by logging the error message.
    """
    logger.error(error_message)

def handle_warning(warning_message):
    """
    Handle warnings by logging the warning message.
    """
    logger.warning(warning_message)

def handle_info(info_message):
    """
    Handle info messages by logging the info message.
    """
    logger.info(info_message)

def handle_debug(debug_message):
    """
    Handle debug messages by logging the debug message.
    """
    logger.debug(debug_message)

def handle_critical(critical_message):
    """
    Handle critical errors by logging the critical error message.
    """
    logger.critical(critical_message)

def handle_fatal(fatal_message):
    """
    Handle fatal errors by logging the fatal error message.
    """
    logger.fatal(fatal_message)

def handle_custom(log_level, message):
    """
    Handle custom log messages by logging the message with the specified log level.
    """
    logger.log(log_level, message)
