import logging
import sys

logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)

def handle_exception(exc_type, exc_value, exc_traceback):
    """
    Handle exceptions by logging the exception message and traceback.

    Args:
        exc_type (type): The type of the exception.
        exc_value (Exception): The exception instance.
        exc_traceback (traceback): The traceback object.
    """
    logger.error("Exception occurred:", exc_info=(exc_type, exc_value, exc_traceback))

def handle_error(error_message):
    """
    Handle errors by logging the error message.

    Args:
        error_message (str): The error message.
    """
    logger.error(error_message)

def handle_warning(warning_message):
    """
    Handle warnings by logging the warning message.

    Args:
        warning_message (str): The warning message.
    """
    logger.warning(warning_message)

def handle_info(info_message):
    """
    Handle info messages by logging the info message.

    Args:
        info_message (str): The info message.
    """
    logger.info(info_message)

def handle_debug(debug_message):
    """
    Handle debug messages by logging the debug message.

    Args:
        debug_message (str): The debug message.
    """
    logger.debug(debug_message)

def handle_critical(critical_message):
    """
    Handle critical errors by logging the critical error message.

    Args:
        critical_message (str): The critical error message.
    """
    logger.critical(critical_message)

def handle_fatal(fatal_message):
    """
    Handle fatal errors by logging the fatal error message.

    Args:
        fatal_message (str): The fatal error message.
    """
    logger.fatal(fatal_message)

def handle_custom(log_level, message):
    """
    Handle custom log messages by logging the message with the specified log level.

    Args:
        log_level (int): The log level.
        message (str): The log message.
    """
    logger.log(log_level, message)
