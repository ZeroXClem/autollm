# tests/test_git_utils.py

from pathlib import Path
from unittest import TestCase, mock

from autollm.utils.git_utils import clone_or_pull_repository


class TestGitUtils(TestCase):
    @mock.patch('autollm.utils.git_utils.Repo')
    def test_clone_new_repository(self, mock_repo):
        git_url = 'https://github.com/example/repo.git'
        local_path = Path('/path/to/local/repo')

        clone_or_pull_repository(git_url, local_path)

        mock_repo.clone_from.assert_called_once_with(git_url, str(local_path))

    @mock.patch('autollm.utils.git_utils.Repo')
    def test_pull_changes_from_existing_repository(self, mock_repo):
        git_url = 'https://github.com/example/repo.git'
        local_path = Path('/path/to/local/repo')

        repo_instance = mock_repo.return_value
        repo_instance.remotes.origin.pull.return_value = None

        clone_or_pull_repository(git_url, local_path)

        repo_instance.remotes.origin.pull.assert_called_once()

    @mock.patch('autollm.utils.git_utils.Repo')
    def test_handle_invalid_git_repository(self, mock_repo):
        git_url = 'https://github.com/example/repo.git'
        local_path = Path('/path/to/local/repo')

        mock_repo.side_effect = mock.Mock(side_effect=InvalidGitRepositoryError)

        with self.assertRaises(InvalidGitRepositoryError):
            clone_or_pull_repository(git_url, local_path)

        mock_repo.assert_called_once_with(str(local_path))
