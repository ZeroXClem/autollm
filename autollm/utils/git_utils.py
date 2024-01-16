from pathlib import Path

from autollm.utils.logging import logger


def clone_or_pull_repository_with_error_handling(git_url: str, local_path: Path) -> None:
    """
    Clone a Git repository or pull latest changes if it already exists.

    Parameters:
        git_url (str): The URL of the Git repository.
        local_path (Path): The local path where the repository will be cloned or updated.
    """
    # Lazy import to avoid dependency on GitPython
    try:
        import subprocess
        import sys
        
        from autollm.utils.logging import logger
        from autollm.utils.shell_utils import run_shell_command
        
        
        def clone_or_pull_repository_with_error_handling(git_url: str, local_path: Path) -> None:
            """
            Clone a Git repository or pull latest changes if it already exists.
        
            Parameters:
                git_url (str): The URL of the Git repository.
                local_path (Path): The local path where the repository will be cloned or updated.
            """
            # Check if Git is installed
            try:
                run_shell_command(['git', '--version'])
            except subprocess.CalledProcessError:
                logger.error('Git is not installed. Please install Git to use this feature.')
                sys.exit(1)
        
            if local_path.exists():
    except ImportError:
        logger.error(
            'GitPython is not installed. Please "pip install gitpython==3.1.37" to use this feature.')
        raise

    if local_path.exists():
        try:
            run_shell_command(['git', 'ls-remote', git_url])
        except subprocess.CalledProcessError:
            logger.error('The Git repository URL is not accessible.')
            sys.exit(1)
    
        # Clone or pull the repository
        if local_path.exists():
            try:
                run_shell_command(['git', '-C', str(local_path), 'pull'])
            except subprocess.CalledProcessError:
                logger.error('Failed to pull the Git repository.')
                sys.exit(1)
        else:
            try:
                run_shell_command(['git', 'clone', git_url, str(local_path)])
            except subprocess.CalledProcessError:
                logger.error('Failed to clone the Git repository.')
                sys.exit(1)
