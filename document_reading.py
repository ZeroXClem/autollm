from autollm import read_files_as_documents
from autollm.utils.git_utils import clone_or_pull_repository
from git import InvalidGitRepositoryError, Repo

# Existing code...

def read_github_repo_as_documents(
        git_repo_url: str,
        relative_folder_path: Optional[str] = None,
        required_exts: Optional[List[str]] = None) -> Sequence[Document]:
    """
    A document provider that fetches documents from a specific folder within a GitHub repository.

    Parameters:
        git_repo_url (str): The URL of the GitHub repository.
        relative_folder_path (str, optional): The relative path from the repo root to the folder containing documents.
        required_exts (Optional[List[str]]): List of required extensions.

    Returns:
        Sequence[Document]: A sequence of Document objects.
    """

    # Ensure the temp_dir directory exists
    temp_dir = Path("autollm/temp/")
    temp_dir.mkdir(parents=True, exist_ok=True)

    logger.info(f"Cloning github repo {git_repo_url} into temporary directory {temp_dir}..")

    try:
        # Clone or pull the GitHub repository to get the latest documents
        clone_or_pull_repository(git_repo_url, temp_dir)

        # Specify the path to the documents
        docs_path = temp_dir if relative_folder_path is None else (temp_dir / Path(relative_folder_path))

        # Read and process the documents
        documents = read_files_as_documents(input_dir=str(docs_path), required_exts=required_exts)
        # Logging (assuming logger is configured)
        logger.info(f"Operations complete, deleting temporary directory {temp_dir}..")
    finally:
        # Delete the temporary directory
        shutil.rmtree(temp_dir, onerror=on_rm_error)

    return documents

# Existing code...
