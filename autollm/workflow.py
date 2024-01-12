from autollm.utils.db_utils import (connect_vectorstore,
                                    initialize_pinecone_index,
                                    initialize_qdrant_index,
                                    update_vector_store_index)
from autollm.utils.document_reading import (read_github_repo_as_documents,
                                            read_webpage_as_documents,
                                            read_website_as_documents)
from autollm.utils.git_utils import clone_or_pull_repository


def run_workflow():
    # Read documents from a GitHub repository
    github_documents = read_github_repo_as_documents("https://github.com/username/repo")

    # Read documents from a website or sitemap
    website_documents = read_website_as_documents(parent_url="https://example.com")

    # Read documents from a single webpage URL
    webpage_documents = read_webpage_as_documents("https://example.com/page")

    # Clone or pull the GitHub repository
    clone_or_pull_repository("https://github.com/username/repo", "local_path")

    # Initialize the Pinecone index
    initialize_pinecone_index("index_name")

    # Initialize the Qdrant index
    initialize_qdrant_index("index_name")

    # Connect to the vector store
    connect_vectorstore(vector_store, index_name="index_name")

    # Update the vector store index with new documents
    update_vector_store_index(vector_store_index, github_documents + website_documents + webpage_documents)
