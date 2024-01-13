# autollm/utils/error_handling.py

class MissingParameterError(ValueError):
    """
    Error raised when a required parameter is missing.
    """
    pass


class UnsupportedExtensionError(ValueError):
    """
    Error raised when an unsupported file extension is encountered.
    """
    pass
