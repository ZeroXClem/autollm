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
        from git import InvalidGitRepositoryError, Repo
    except ImportError:
        logger.error(
            'GitPython is not installed. Please "pip install gitpython==3.1.37" to use this feature.')
        raise

    try:
        if local_path.exists():
            repo = Repo(str(local_path))
            repo.remotes.origin.pull()
        else:
            Repo.clone_from(git_url, str(local_path))
    except Exception as e:
        logger.error(f"An error occurred while handling the repository: {e}")
