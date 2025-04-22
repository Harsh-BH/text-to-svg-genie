# Contributing to Text-to-SVG Genie

Thank you for considering contributing to Text-to-SVG Genie! This document provides guidelines and instructions for contributing to this project.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Contribution Workflow](#contribution-workflow)
- [Coding Standards](#coding-standards)
- [Testing Guidelines](#testing-guidelines)
- [Documentation](#documentation)
- [Issue Reporting](#issue-reporting)
- [Pull Request Process](#pull-request-process)
- [Community](#community)

## Code of Conduct

By participating in this project, you agree to abide by our Code of Conduct. Please be respectful and considerate of others when contributing to the project.

## Getting Started

Before you begin:

1. Make sure you have a [GitHub account](https://github.com/signup)
2. Familiarize yourself with [Git](https://git-scm.com/)
3. Read the project [README.md](README.md) to understand the project goals and features

## Development Setup

1. **Fork the repository** on GitHub
2. **Clone your fork locally**:
   ```bash
   git clone https://github.com/YOUR-USERNAME/text-to-svg-genie.git
   cd text-to-svg-genie
   ```
3. **Set up a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
4. **Install the development dependencies**:
   ```bash
   pip install -r requirements.txt
   pip install -e .  # Install the package in development mode
   ```
5. **Set up pre-commit hooks**:
   ```bash
   pip install pre-commit
   pre-commit install
   ```

## Contribution Workflow

1. **Create a new branch** for your feature or bugfix:
   ```bash
   git checkout -b feature/your-feature-name
   # or
   git checkout -b fix/issue-you-are-fixing
   ```
2. **Make your changes** and commit them with clear messages:
   ```bash
   git add .
   git commit -m "Descriptive commit message"
   ```
3. **Push to your fork**:
   ```bash
   git push origin feature/your-feature-name
   ```
4. **Submit a pull request** to the main repository

## Coding Standards

We follow PEP 8 style guidelines for Python code. Key points to remember:

- Use 4 spaces for indentation (not tabs)
- Maximum line length of 88 characters
- Write docstrings for all classes, methods, and functions
- Use descriptive variable names
- Include type hints where appropriate

We use the following tools to maintain code quality:

- **Black** for code formatting
- **isort** for import sorting
- **flake8** for style guide enforcement
- **mypy** for static type checking

You can run these tools with:

```bash
black .
isort .
flake8
mypy .
```

## Testing Guidelines

- Write tests for all new functionality
- Make sure all tests pass before submitting a pull request
- Aim for high test coverage

Run the test suite with:

```bash
pytest
```

## Documentation

- Keep the README.md updated with any relevant changes
- Document all public functions, classes, and methods
- Add comments for complex code sections
- Update documentation when changing functionality

## Issue Reporting

When reporting issues, please include:

1. A clear and descriptive title
2. Steps to reproduce the issue
3. Expected behavior
4. Actual behavior
5. Environment details (OS, Python version, etc.)
6. Any relevant logs or screenshots

## Pull Request Process

1. Ensure your code follows the coding standards
2. Update documentation as necessary
3. Include tests that validate your changes
4. Make sure all tests pass
5. Link the PR to any related issues
6. Wait for code review and address any feedback

Your PR should include:
- A clear description of changes
- Any new dependencies introduced
- How your changes were tested
- Screenshots for UI changes (if applicable)

## Branch Naming Conventions

Use the following naming conventions for branches:

- `feature/feature-name` for new features
- `fix/issue-description` for bug fixes
- `docs/documentation-change` for documentation changes
- `refactor/refactor-description` for code refactoring
- `test/test-description` for test additions or changes

## Community

Join our community discussions:

- For general questions, use [Discussions](https://github.com/yourusername/text-to-svg-genie/discussions)
- For bug reports and feature requests, use [Issues](https://github.com/yourusername/text-to-svg-genie/issues)

---

Thank you for contributing to Text-to-SVG Genie!
