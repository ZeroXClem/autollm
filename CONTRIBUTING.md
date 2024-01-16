# Contributing to AutoLLM 🌟

Thank you for considering a contribution to AutoLLM. Your input is invaluable to our project's continued growth and improvement.

## PR Guidelines 📝

To streamline the integration of your contributions:

- **Start by forking the repository 🍴**: This allows you to work on your own copy of the project. Refer to the [GitHub documentation](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request-from-a-fork) for steps to open a PR from your fork.

- **New Branch 🌱**: Always create a new branch from the `main` branch for your PR. It keeps things neat and makes the review process smoother.

- **Size Matters 📏**: Aim for smaller PRs. If you have a big feature in mind, consider breaking it up. It helps us understand your contribution better and gets you feedback quicker!

- **Stay Current 🕰️**: Ensure your PR is synchronized with the latest updates from the `safevideo/autollm` `main` branch. If your branch is outdated, update it using the 'Update branch' button or by executing `git pull` and `git merge main`.

## Code Standards and Pre-commit Hooks 🛠️

Maintaining a consistent codebase is crucial. We utilize tools such as [flake8](https://flake8.pycqa.org/en/latest/) and [isort](https://pycqa.github.io/isort/) to achieve this. In addition, we use pre-commit hooks to automate code checks and formatting. See the `Pre-commit Hooks` section below for setup instructions.

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
