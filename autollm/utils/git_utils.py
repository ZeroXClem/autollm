from pathlib import Path

import logging


def clone_or_pull_repository(git_url: str, local_path: Path) -> None:
    """
    Clone a Git repository or pull latest changes if it already exists.

    Parameters:
        git_url (str): The URL of the Git repository.
        local_path (Path): The local path where the repository will be cloned or updated.
    """
    # Lazy import to avoid dependency on GitPython
    try:
        from git import InvalidGitRepositoryError
from git import Repo
    except (InvalidGitRepositoryError, TypeError) as e:
        raise ImportError(f'Error while cloning or pulling the repository: {e}')
        return None
    except ImportError as e:
        logger.error(f'Error: {e}. Please "pip install gitpython==3.1.37" to use this feature.')
        raise

    if local_path.exists(): 
        try:
            repo = Repo(str(local_path))
            repo.remotes.origin.pull()
        except InvalidGitRepositoryError:
            # The existing directory is not a valid git repo, clone anew
            from git import Repo
repo.clone_from(git_url, str(local_path))
        except InvalidGitRepositoryError:
            # The existing directory is not a valid git repo, clone anew
            logging.error('Error while pulling the repository: Failed to pull the latest changes')
    else:
        Repo.clone_from(git_url, str(local_path))
