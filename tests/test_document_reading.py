import os
import shutil
import stat
import unittest
from pathlib import Path
from unittest.mock import patch

from autollm.utils.document_reading import (on_rm_error,
                                            read_files_as_documents,
                                            read_github_repo_as_documents,
                                            read_webpage_as_documents,
                                            read_website_as_documents)


class TestDocumentReading(unittest.TestCase):
    def setUp(self):
        self.test_dir = Path("tests/temp/")
        self.test_dir.mkdir(parents=True, exist_ok=True)

    def tearDown(self):
        shutil.rmtree(self.test_dir, onerror=on_rm_error)

    def test_read_files_as_documents_from_directory(self):
        # Create test files in the test directory
        file1 = self.test_dir / "file1.md"
        file1.write_text("Test content 1")
        file2 = self.test_dir / "file2.md"
        file2.write_text("Test content 2")

        # Call the function to read files as documents
        documents = read_files_as_documents(input_dir=str(self.test_dir))

        # Assert that the correct number of documents are returned
        self.assertEqual(len(documents), 2)

        # Assert that the document content is correct
        self.assertEqual(documents[0].content, "Test content 1")
        self.assertEqual(documents[1].content, "Test content 2")

    def test_read_files_as_documents_from_file_list(self):
        # Create test files in the test directory
        file1 = self.test_dir / "file1.md"
        file1.write_text("Test content 1")
        file2 = self.test_dir / "file2.md"
        file2.write_text("Test content 2")

        # Call the function to read files as documents
        documents = read_files_as_documents(input_files=[str(file1), str(file2)])

        # Assert that the correct number of documents are returned
        self.assertEqual(len(documents), 2)

        # Assert that the document content is correct
        self.assertEqual(documents[0].content, "Test content 1")
        self.assertEqual(documents[1].content, "Test content 2")

    def test_read_files_as_documents_exclude_hidden(self):
        # Create test files in the test directory
        file1 = self.test_dir / "file1.md"
        file1.write_text("Test content 1")
        hidden_file = self.test_dir / ".hidden.md"
        hidden_file.write_text("Hidden content")

        # Call the function to read files as documents with exclude_hidden=True
        documents = read_files_as_documents(input_dir=str(self.test_dir), exclude_hidden=True)

        # Assert that only the non-hidden file is returned as a document
        self.assertEqual(len(documents), 1)
        self.assertEqual(documents[0].content, "Test content 1")

    def test_read_files_as_documents_filename_as_id(self):
        # Create test files in the test directory
        file1 = self.test_dir / "file1.md"
        file1.write_text("Test content 1")

        # Call the function to read files as documents with filename_as_id=False
        documents = read_files_as_documents(input_dir=str(self.test_dir), filename_as_id=False)

        # Assert that the document ID is the full file path
        self.assertEqual(len(documents), 1)
        self.assertEqual(documents[0].id_, str(file1))

    def test_read_files_as_documents_recursive(self):
        # Create nested test directories and files
        nested_dir = self.test_dir / "nested"
        nested_dir.mkdir()
        file1 = nested_dir / "file1.md"
        file1.write_text("Test content 1")

        # Call the function to read files as documents with recursive=True
        documents = read_files_as_documents(input_dir=str(self.test_dir), recursive=True)

        # Assert that the nested file is returned as a document
        self.assertEqual(len(documents), 1)
        self.assertEqual(documents[0].content, "Test content 1")

    def test_read_files_as_documents_with_required_exts(self):
        # Create test files in the test directory with different extensions
        file1 = self.test_dir / "file1.md"
        file1.write_text("Test content 1")
        file2 = self.test_dir / "file2.pdf"
        file2.write_text("Test content 2")

        # Call the function to read files as documents with required_exts=[".pdf"]
        documents = read_files_as_documents(input_dir=str(self.test_dir), required_exts=[".pdf"])

        # Assert that only the file with the required extension is returned as a document
        self.assertEqual(len(documents), 1)
        self.assertEqual(documents[0].content, "Test content 2")

    @patch("autollm.utils.document_reading.clone_or_pull_repository")
    def test_read_github_repo_as_documents(self, mock_clone_or_pull_repository):
        # Mock the clone_or_pull_repository function
        mock_clone_or_pull_repository.return_value = None

        # Call the function to read GitHub repo as documents
        documents = read_github_repo_as_documents(git_repo_url="https://github.com/example/repo")

        # Assert that the mock function was called
        mock_clone_or_pull_repository.assert_called_once_with(
            git_repo_url="https://github.com/example/repo", local_path=Path("autollm/temp/")
        )

        # Assert that the correct number of documents are returned
        self.assertEqual(len(documents), 0)

    def test_read_website_as_documents(self):
        # Call the function to read website as documents
        documents = read_website_as_documents(parent_url="https://example.com")

        # Assert that the correct number of documents are returned
        self.assertEqual(len(documents), 0)

    def test_read_webpage_as_documents(self):
        # Call the function to read webpage as documents
        documents = read_webpage_as_documents(url="https://example.com")

        # Assert that the correct number of documents are returned
        self.assertEqual(len(documents), 0)


if __name__ == "__main__":
    unittest.main()
