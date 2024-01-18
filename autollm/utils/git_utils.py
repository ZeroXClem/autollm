from pathlib import Path

from autollm.utils.logging import logger


def clone_or_pull_repository(git_url: str, local_path: Path) -> None:
    """
    Clone a Git repository or pull latest changes if it already exists.

    Parameters:
        git_url (str): The URL of the Git repository.
        local_path (Path): The local path where the repository will be cloned or updated.

    Raises:
        Exception: If an error occurs during the cloning or pulling process.
    """
    """
    Clone a Git repository or pull latest changes if it already exists.

    Parameters:
        git_url (str): The URL of the Git repository.
        local_path (Path): The local path where the repository will be cloned or updated.
    """
    try:
        import logging
        from git import InvalidGitRepositoryError, Repo
    except ImportError:
        logger.error(
            'GitPython is not installed. Please "pip install gitpython==3.1.37" to use this feature.')
        raise
    try:
        import logging
        from git import InvalidGitRepositoryError, Repo
    except ImportError:
        logger.error(
            'GitPython is not installed. Please "pip install gitpython==3.1.37" to use this feature.')
        raise

    if local_path.exists():
        try:
            repo = Repo(str(local_path))
            repo.remotes.origin.pull()
        except InvalidGitRepositoryError:
            # The existing directory is not a valid git repo, clone anew
            try:
                Repo.clone_from(git_url, str(local_path))
            except Exception as e:
                logger.error(f'Error occurred during cloning: {e}')
                raise e
    else:
        Repo.clone_from(git_url, str(local_path))
    logger.info(f"Pulling latest changes from {git_url} into {local_path}..")
    repo.remotes.origin.pull()
    logger.info("Pull successful.")
except InvalidGitRepositoryError:
    logger.info(f"Cloning {git_url} into {local_path}..")
    Repo.clone_from(git_url, str(local_path))
    logger.info("Clone successful.")
