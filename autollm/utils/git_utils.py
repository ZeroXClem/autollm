from pathlib import Path

from autollm.utils.logging import logger


def clone_or_pull_repository(git_url: str, local_path: Path) -> None:
    """
    Clone a Git repository or pull latest changes if it already exists.

    Parameters:
        git_url (str): The URL of the Git repository.
        local_path (Path): The local path where the repository will be cloned or updated.
    """
    # Lazy import to avoid dependency on GitPython
    try:
    repo = None
    logger.info(f'Detecting if git repository exists at {local_path}..')
    if local_path.exists():
        try:
            repo = Repo(str(local_path))
            repo.remotes.origin.pull()
            logger.info(f'Pulling latest changes from {git_url} into {local_path}..')
            logger.info('Pull successful.')
        except InvalidGitRepositoryError:
            # The existing directory is not a valid git repo, clone anew
            logger.info(f'Pull failed: {local_path} is not a valid git repository.')
            repo = None
            raise
    else:
        logger.info(f'Cloning {git_url} into {local_path}..')
        repo = Repo.clone_from(git_url, str(local_path))
        logger.info('Clone successful.')
except Exception as e:
    logger.error(f'Error in cloning or pulling the Git repository: {e}')
    return None
    repo = None
    logger.info(f'Detecting if git repository exists at {local_path}..')
    if local_path.exists():
        try:
            repo = Repo(str(local_path))
            repo.remotes.origin.pull()
            logger.info(f'Pulling latest changes from {git_url} into {local_path}..')
            logger.info('Pull successful.')
        except InvalidGitRepositoryError:
            # The existing directory is not a valid git repo, clone anew
            logger.info(f'Pull failed: {local_path} is not a valid git repository.')
            repo = None
            raise
    else:
        logger.info(f'Cloning {git_url} into {local_path}..')
        repo = Repo.clone_from(git_url, str(local_path))
        logger.info('Clone successful.')
except Exception as e:
    logger.error(f'Error in cloning or pulling the Git repository: {e}')
    return None
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
            Repo.clone_from(git_url, str(local_path))
    else:
        Repo.clone_from(git_url, str(local_path))
    logger.info(f"Pulling latest changes from {git_url} into {local_path}..")
    repo.remotes.origin.pull()
    logger.info("Pull successful.")
except InvalidGitRepositoryError:
    logger.info(f"Cloning {git_url} into {local_path}..")
    Repo.clone_from(git_url, str(local_path))
    logger.info("Clone successful.")
