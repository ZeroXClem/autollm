from pathlib import Path

from autollm.utils.logging import logger


def clone_or_pull_repository(git_url: str, local_path: Path) -> None:
    """Clone a Git repository or pull latest changes if it already exists.

    Args:
        git_url (str): The URL of the Git repository.
        local_path (Path): The local path where the repository will be cloned or updated.
    Returns:
        None
    """
    # Lazy import to avoid dependency on GitPython
    try:
        from git import InvalidGitRepositoryError, Repo, GitCommandError
    except ImportError:
        logger.error(
            'GitPython is not installed. Please "pip install gitpython==3.1.37" to use this feature.')
        raise

    if local_path.exists():
        try:
            repo = Repo(str(local_path))
            repo.remotes.origin.pull()
        except (InvalidGitRepositoryError, GitCommandError):
            # The existing directory is not a valid git repo or there was an error pulling, clone anew
            Repo.clone_from(git_url, str(local_path))
    except InvalidGitRepositoryError:
        Repo.clone_from(git_url, str(local_path))
    except GitCommandError:
        logger.error(f"Error pulling changes from {git_url}. Cloning anew..")
        Repo.clone_from(git_url, str(local_path))
    return None
