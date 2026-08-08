# Shell Project Template

[![GitHub Stars](https://img.shields.io/github/stars/diablo02000/shell-repository-template-local?style=social)](https://github.com/diablo02000/shell-repository-template-local/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub Actions](https://github.com/diablo02000/shell-repository-template/actions/workflows/linter.yml/badge.svg)](https://github.com/diablo02000/shell-repository-template-local/actions/workflows/linter.yml)
[![Copier](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/copier-org/copier/master/img/badge/badge-grayscale-inverted-border-orange.json)](https://github.com/copier-org/copier)
[![semantic-release: angular](https://img.shields.io/badge/semantic--release-angular-e10079?logo=semantic-release)](https://github.com/semantic-release/semantic-release)

**A production-ready Copier template for Bash/shell script projects with batteries included.**

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
  - [Adding New Scripts](#adding-new-scripts)
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
| **Mise Integration** | Automatic tool version management (bats, shellcheck, shfmt) |
| **Bats Testing** | Robust testing framework with support/assert libraries |
| **Pre-commit Hooks** | Automatic code quality checks before commits |
| **GitHub Actions** | CI/CD pipelines for linting, testing, and releases |
| **Semantic Release** | Automated version management and changelog generation |
| **Shellcheck + Shfmt** | Static analysis and code formatting |
| **Gitleaks Integration** | Prevent accidental credential commits |
| **Markdown Linting** | Consistent documentation formatting |

---

## Quick Start

### Prerequisites

- Git
- [Copier](https://copier.readthedocs.io/) (v9.0+ recommended)
- Bash 4.0+

### Create Your Project

```bash
# Create project from template
copier copy gh:diablo02000/shell-repository-template-local my-shell-project
cd my-shell-project

# Answer the configuration prompts
# (project name, description, author, etc.)

# Install development dependencies
mise install

# Run tests to verify everything works
mise run test
```

---

## Project Structure

```text
my-shell-project/
├── .github/                  # GitHub configuration
│   └── workflows/           # CI/CD pipelines
│       ├── linter.yml       # Linting workflow
│       ├── unit-tests.yml   # Test workflow
│       └── release.yml      # Release workflow
├── .mise.toml               # Development tool configuration
├── .pre-commit-config.yaml  # Pre-commit hooks
├── README.md                 # Project documentation
├── src/                     # Your shell scripts
│   └── script.sh            # Main script (customizable)
├── tests/                   # Bats test suite
│   ├── test_*.bats          # Test files
│   └── test_helper/         # Test libraries (auto-downloaded)
│       ├── bats-support/
│       └── bats-assert/
├── .gitignore               # Git ignore patterns
└── LICENSE                  # Project license
```

---

## Template Configuration

### Available Variables

| Variable | Description | Default |
| ---------- | ------------- | --------- |
| `project_name` | Project name | my-bash-project |
| `project_description` | Project description | "" |
| `author_name` | Author name | Your Name |
| `author_email` | Author email | "your.email@example.com" |
| `repo_owner` | GitHub username/org | your_github_username |
| `main_script` | Main script filename | script.sh |
| `license` | Project license | MIT |

### Customization Example

```bash
copier copy gh:diablo02000/shell-repository-template-local my-project \
  --data project_name=my-awsome-cli \
  --data project_description="A CLI tool for awesome things" \
  --data main_script=my-cli.sh
```

---

## Development

### Install Dependencies

```bash
# Install mise (if not already installed)
curl https://mise.run | sh

# Install project tools
mise install
```

### Available Tasks

| Command | Description |
| --------- | ------------- |
| `mise run test` | Run all bats tests |
| `mise run lint` | Run shellcheck and shfmt |
| `mise run setup` | Install pre-commit hooks |

### Adding New Scripts

1. Create your script in `src/`
2. Make it executable: `chmod +x src/my-script.sh`
3. Add tests in `tests/test_my-script.bats`
4. Run `mise run test` to verify

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

- Best practices for shell scripting
- Comprehensive testing setup
- Automatic code quality enforcement
- Professional documentation standards

### Can I customize the template?

Yes! After generating your project, you can:

- Modify any files
- Add new scripts
- Change the configuration
- Extend the CI/CD pipelines

### How do I add new dependencies?

Edit `.mise.toml` and run `mise install`.

---

## Support

- **Issues**: [GitHub Issues](https://github.com/diablo02000/shell-repository-template-local/issues)
- **Discussions**: [GitHub Discussions](https://github.com/diablo02000/shell-repository-template-local/discussions)
- **Contribute**: Pull requests welcome!

---

**Star this repository if you find it useful!**
