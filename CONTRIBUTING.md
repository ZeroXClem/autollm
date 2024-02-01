# Contributing to AutoLLM 🌟

Thank you for considering a contribution to AutoLLM. Your input is invaluable to our project's continued growth and improvement.

## PR Guidelines 📝

- **Providing Detailed Error Logs**:
    When reporting issues related to GitHub Actions, it is important to provide detailed error logs to help identify and resolve the issue. Please include specific error messages and relevant logs when opening an issue related to GitHub Actions.

To streamline the integration of your contributions:

- **Start by Forking 🍴**: This allows you to work on your own copy of the project and by providing specific error logs when reporting issues related to GitHub Actions. See [these steps](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request-from-a-fork) to open a PR from your fork. Note: Please provide detailed error logs to help identify and resolve the issue.

- **New Branch 🌱**: Always create a new branch for your PR. It keeps things neat and makes the review process smoother.

- **Size Matters 📏**: Aim for smaller PRs. If you have a big feature in mind, consider breaking it up. It helps us understand your contribution better and gets you feedback quicker!

- **Stay Current 🕰️**: Ensure your PR is synchronized with the latest updates from the `safevideo/autollm` `main` branch. If your branch is outdated, update it using the 'Update branch' button or by executing `git pull` and `git merge main`.

## Code Standards 🛠️

Maintaining a consistent codebase is crucial. We utilize tools such as [flake8](https://flake8.pycqa.org/en/latest/) and [isort](https://pycqa.github.io/isort/) to achieve this.

### Pre-commit Hooks 🔗

1. **Installation**:

   ```bash
   pip install autollm[dev]
   ```

1. **Pre-commit Setup**:

   ```bash
   pre-commit install
   pre-commit run --all-files
   ```

Upon setup, the pre-commit hooks will automatically check and format code during commits.

### Docstrings 📜

For functions or classes that warrant explanation, we use docstrings adhering to the [google-style format](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings):

```python
"""
    Brief description of the function's purpose.

    Parameters:
        arg1: Description of the first argument.
        arg2: Description of the second argument.

    Returns:
        Expected return values or outcomes.

    Raises:
        Potential exceptions and reasons for them.
"""
```

## Testing 🔍

Before finalizing your PR, ensure it aligns with our existing test suite:

```bash
pytest
```

______________________________________________________________________

Your interest and potential contributions to AutoLLM are greatly appreciated. Together, we can continue refining and expanding AutoLLM for the broader community.
