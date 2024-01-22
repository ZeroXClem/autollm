from autollm import read_files_as_documents
from autollm.utils.git_utils import clone_or_pull_repository


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

    try:
        clone_or_pull_repository(git_repo_url, relative_folder_path)
        docs_path = Path("autollm/temp/") if relative_folder_path is None else (Path("autollm/temp/") / Path(relative_folder_path))
        documents = read_files_as_documents(input_dir=str(docs_path), required_exts=required_exts)
        logger.info(f"Operations complete, deleting temporary directory {docs_path}..")
    except Exception as e:
        logger.error(f"An error occurred during cloning or pulling the repository: {str(e)}")
        raise

    return documents
