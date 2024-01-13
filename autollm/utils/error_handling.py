import logging
import os
import shutil
import stat
from pathlib import Path
from typing import Callable, Tuple

from autollm.utils.logging import logger


def on_rm_error(func: Callable, path: str, exc_info: Tuple):
    """
    Error handler for `shutil.rmtree` to handle permission errors.

    Parameters:
        func (Callable): The function that raised the error.
        path (str): The path to the file or directory which couldn't be removed.
        exc_info (Tuple): Exception information returned by sys.exc_info().
    """
    os.chmod(path, stat.S_IWRITE)
    os.unlink(path)


def handle_error(error_message: str, stack_trace: str):
    """
    Handle error logging and reporting.

    Parameters:
        error_message (str): The error message to log and report.
        stack_trace (str): The stack trace of the error.
    """
    logger.error(error_message)
    logger.debug(stack_trace)


# Modify the read_files_as_documents function in document_reading.py to add error handling
def read_files_as_documents(
        input_dir: str,
        exclude_hidden: bool = True,
        filename_as_id: bool = True,
        recursive: bool = True,
        required_exts: list = None,
        show_progress: bool = True,
        **kwargs) -> list:
    """
    Process markdown files to extract documents using SimpleDirectoryReader.

    Parameters:
        input_dir (str): Path to the directory containing the markdown files.
        exclude_hidden (bool): Whether to exclude hidden files.
        filename_as_id (bool): Whether to use the filename as the document id.
        recursive (bool): Whether to recursively search for files in the input directory.
        required_exts (list): List of file extensions to be read. Defaults to all supported extensions.
        show_progress (bool): Whether to show progress while reading files.
        **kwargs: Additional keyword arguments.

    Returns:
        documents (list): A list of Document objects.
    """
    try:
        # Existing code block
        # ...

    except Exception as e:
        error_message = f"Error occurred while reading files from {input_dir}: {str(e)}"
        stack_trace = traceback.format_exc()
        handle_error(error_message, stack_trace)

    return documents
