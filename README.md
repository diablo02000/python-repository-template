# Python Project Template

[![GitHub Stars](https://img.shields.io/github/stars/diablo02000/python-repository-template?style=social)](https://github.com/diablo02000/python-repository-template/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/python-3.12%2B-blue?logo=python&logoColor=white)](https://python.org)
[![pytest](https://img.shields.io/badge/test-pytest-0A9EDC?logo=pytest)](https://docs.pytest.org/)
[![ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![mypy](https://img.shields.io/badge/type-mypy-316192?logo=mypy)](https://mypy-lang.org/)
[![uv](https://img.shields.io/badge/package-uv-00A3E0?logo=uv)](https://github.com/astral-sh/uv)
[![Copier](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/copier-org/copier/master/img/badge/badge-grayscale-inverted-border-orange.json)](https://github.com/copier-org/copier)
[![semantic-release: angular](https://img.shields.io/badge/semantic--release-angular-e10079?logo=semantic-release)](https://github.com/semantic-release/semantic-release)

**A production-ready Copier template for Python projects with batteries included.**

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
"**Table of Contents**"

- [Features](#features)
- [Quick Start](#quick-start)
  - [Prerequisites](#prerequisites)
  - [Create Your Project](#create-your-project)
- [Project Structure](#project-structure)
- [Template Configuration](#template-configuration)
  - [Available Variables](#available-variables)
  - [Customization Example](#customization-example)
- [Development](#development)
  - [Install Dependencies](#install-dependencies)
  - [Available Tasks](#available-tasks)
  - [Adding New Modules](#adding-new-modules)
- [Contributing](#contributing)
- [License](#license)
- [Changelog](#changelog)
- [FAQ](#faq)
  - [Why use this template?](#why-use-this-template)
  - [Can I customize the template?](#can-i-customize-the-template)
  - [How do I add new dependencies?](#how-do-i-add-new-dependencies)
- [Support](#support)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

---

## Features

| Feature | Benefit |
| --------- | --------- |
| **Python 3.12+ Support** | Modern Python features and type hints |
| **pytest Testing** | Comprehensive testing framework with coverage support |
| **ruff Integration** | Fast linting and formatting (replaces black, isort, flake8, etc.) |
| **mypy Type Checking** | Static type checking for robust code |
| **uv Package Management** | Fast dependency management and builds |
| **Mise Integration** | Automatic tool version management (Python, uv, ruff, mypy) |
| **Pre-commit Hooks** | Automatic code quality checks before commits |
| **GitHub Actions** | CI/CD pipelines for linting, testing, and releases |
| **Semantic Release** | Automated version management and changelog generation |
| **Gitleaks Integration** | Prevent accidental credential commits |
| **Markdown Linting** | Consistent documentation formatting |
| **Copier Template** | Easy project scaffolding and customization |

---

## Quick Start

### Prerequisites

- Git
- [Copier](https://copier.readthedocs.io/) (v9.0+ recommended)
- Python 3.12+

### Create Your Project

```bash
# Create project from template
copier copy gh:diablo02000/python-repository-template my-python-project
cd my-python-project

# Answer the configuration prompts
# (project name, description, author, etc.)

# Install development dependencies
mise install

# Sync project dependencies and install pre-commit hooks
mise run setup

# Run tests to verify everything works
mise run test
```

---

## Project Structure

```text
my-python-project/
├── .github/                  # GitHub configuration
│   └── workflows/           # CI/CD pipelines
│       ├── pytest.yml       # Python test and lint workflow
│       ├── linter.yml       # Linting workflow
│       └── release.yml      # Release workflow
├── .mise.toml               # Development tool configuration
├── .pre-commit-config.yaml  # Pre-commit hooks
├── .python-version          # Python version specification
├── pyproject.toml           # Project configuration and dependencies
├── README.md                 # Project documentation
├── src/                     # Your Python source code
│   └── {{project_name}}/    # Python package
│       ├── __init__.py     # Package initialization
│       ├── main.py         # Main entry point
│       └── ...             # Additional modules
├── tests/                   # Test suite
│   ├── __init__.py         # Test package initialization
│   ├── conftest.py         # Pytest fixtures
│   ├── test_main.py        # Test files
│   └── integration/        # Integration tests
├── .gitignore               # Git ignore patterns
├── LICENSE                  # Project license
└── renovate.json            # Dependency update configuration
```

---

## Template Configuration

### Available Variables

| Variable | Description | Default |
| ---------- | ------------- | --------- |
| `project_name` | Project name | my-python-project |
| `project_description` | Project description | "" |
| `author_name` | Author name | Your Name |
| `author_email` | Author email | "your.email@example.com" |
| `repo_owner` | GitHub username/org | your_github_username |
| `license` | Project license | MIT |

### Customization Example

```bash
copier copy gh:diablo02000/python-repository-template my-project \
  --data project_name=my-awesome-cli \
  --data project_description="A CLI tool for awesome things" \
  --data author_name="Jane Doe" \
  --data author_email="jane@example.com"
```

---

## Development

### Install Dependencies

```bash
# Install mise (if not already installed)
curl https://mise.run | sh

# Install project tools (Python, uv, ruff, mypy)
mise install
```

### Available Tasks

| Command | Description |
| --------- | ------------- |
| `mise run test` | Run all pytest tests with coverage |
| `mise run test-unit` | Run pytest tests without coverage |
| `mise run test-coverage` | Run tests with HTML coverage report |
| `mise run lint` | Run ruff linting and mypy type checking |
| `mise run format` | Format code with ruff |
| `mise run build` | Build the package with uv |
| `mise run setup` | Install dependencies and pre-commit hooks |
| `mise run clean` | Clean build artifacts and cache files |

### Adding New Modules

1. Create your module in `src/{{project_name}}/`
2. Add tests in `tests/test_*.py`
3. Update `pyproject.toml` if adding new dependencies
4. Run `mise run lint` to check code quality
5. Run `mise run test` to verify

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for contribution guidelines.

---

## License

This template is licensed under the MIT License. Generated projects will have their own license as specified during template configuration.

---

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for template version history.

---

## FAQ

### Why use this template?

This template provides a production-ready foundation with:

- Modern Python development best practices
- Comprehensive testing setup with pytest and coverage
- Automatic code quality enforcement with ruff and mypy
- Fast dependency management with uv
- Professional documentation standards
- Automated CI/CD pipelines

### Can I customize the template?

Yes! After generating your project, you can:

- Modify any files
- Add new modules and packages
- Change the configuration
- Extend the CI/CD pipelines
- Customize the tooling setup

### How do I add new dependencies?

Edit `pyproject.toml` and add your dependencies to the appropriate sections, then run:

```bash
# Sync dependencies with uv
uv sync

# Or install a specific package
uv add package-name
```

---

## Support

- **Issues**: [GitHub Issues](https://github.com/diablo02000/python-repository-template/issues)
- **Discussions**: [GitHub Discussions](https://github.com/diablo02000/python-repository-template/discussions)
- **Contribute**: Pull requests welcome!

---

**Star this repository if you find it useful!**
