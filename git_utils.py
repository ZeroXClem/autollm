import logging

from git import InvalidGitRepositoryError, Repo

logger = logging.getLogger(__name__)

def clone_or_pull_repository(git_url: str, local_path: Path) -> None:
    """
    Clone a Git repository or pull latest changes if it already exists.

    Parameters:
        git_url (str): The URL of the Git repository.
        local_path (Path): The local path where the repository will be cloned or updated.
    """
    try:
        if local_path.exists():
            try:
                repo = Repo(str(local_path))
                repo.remotes.origin.pull()
            except InvalidGitRepositoryError:
                # The existing directory is not a valid git repo, clone anew
                Repo.clone_from(git_url, str(local_path))
        else:
            Repo.clone_from(git_url, str(local_path))
    except Exception as e:
        logger.error(f"An error occurred during cloning or pulling the repository: {str(e)}")
        raise
