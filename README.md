# python-package-template

This package is intentionally simple to provide a clean starting point for your own projects.

## Overview

The tools in this template were chosen to be simple, low friction, effective, and relatively comprehensive.

| Purpose            | Tool      |
| ------------------ | --------- |
| Package Management | uv        |
| Data Validation    | pydantic  |
| CLI Framework      | typer     |
| Testing            | pytest    |
| Code Quality       | ruff      |
| Type Checking      | mypy      |
| Security Audit     | pip-audit |
| Shell Script Lint  | shellcheck|
| Git Hooks          | prek      |


## Installation

### Prerequisites

- Python 3.10 or higher
- [uv](https://github.com/astral-sh/uv) package manager

### Setup

**Option 1: Use this template (recommended)**

Visit https://github.com/AlexAndrewsAI/python-package-template and click the green "Use this template" button to create your own repository. Then clone your new repository:

```bash
cd your-repo-name
uv sync
```

**Option 2: Clone directly**

```bash
git clone https://github.com/AlexAndrewsAI/python-package-template.git
cd python-package-template
uv sync
```

To install the package in editable mode (recommended for development) and test the CLI:

```bash
uv pip install -e .
hello-world --version
```

## Usage

### Basic Example

```python
from python_package_template.hello import HelloWorld
from python_package_template.config import Config

# Create with default name
hello = HelloWorld()
greeting = hello.greet() # Hello, World!

# Create with custom name
hello = HelloWorld(Config(name="Alice"))
personal_greeting = hello.greet() # Hello, Alice!
```

### Configuration

The `Config` class uses **pydantic** for validation:

```python
from python_package_template.config import Config

# Create with default name
config = Config()

# Create with custom name
config = Config(name="Alice")
```

### Command Line Interface

The package includes a CLI tool built with **typer**:

```bash
# Show version
uv run hello-world --version

# Run the CLI with default name
uv run hello-world hello

# Greet a specific name
uv run hello-world hello --name Alice

# Show help
uv run hello-world hello --help
```

## Development

### Install Dev Dependencies

```bash
uv sync --dev
```

This installs all dependencies and dev tools (pytest, ruff, mypy).

### Run Tests

```bash
# Run all tests
uv run pytest

# Run specific test
uv run pytest tests/test_hello.py::test_default_name
```

### Code Quality

```bash
# Lint code
uv run ruff check
uv run ruff format

# Type check
uv run mypy .

# Security audit
uv run pip-audit
```

### Git Hooks with prek

This template uses **prek** for managing pre-commit Git hooks that automatically run code quality checks before commits.

**Install Git hooks (recommended):**

```bash
uv run prek install
```

This installs Git hooks that will automatically run the following checks on every commit:
- pytest (tests)
- ruff check (linting)
- ruff format (formatting)
- mypy (type checking)
- pip-audit (security audit)
- shellcheck (shell script linting)

**Run hooks manually:**

```bash
# Run all hooks on all files
uv run prek run --all-files

# Run hooks on staged files only
uv run prek run
```

### Git Configuration

The `.gitignore` file ignores all dot files (`.*`) by default, with exceptions for `.gitignore`, `.github`, and `.env.example`. If you want to commit other dot files (e.g., `.devin/`, `.cursor/`, etc.), add them to the negation list in `.gitignore`:

```
/.*
!.gitignore
!.github
!.env.example
!.myfile    # Add your custom dot files here
```

## Project Structure

```
python-package-template/
├── AGENTS.md
├── .gitignore
├── pyproject.toml
├── python_package_template
│   ├── cli.py
│   ├── config.py
│   ├── hello.py
│   ├── __init__.py
│   └── py.typed
├── README.md
├── tests
│   ├── __init__.py
│   └── test_hello.py
└── uv.lock
```



## Agent Instructions

This template includes two agent instruction files for different workflows:

### AGENTS.md
Complete instructions for an AI agent with full automation. The agent automatically runs `pytest`, `ruff check`, and `mypy` after code changes to validate quality before handoff.

**Best for:** Fully autonomous workflows where the agent handles all validation.

### AGENTS_MANUAL_CHECKS.md
Streamlined instructions that skip automated validation tools to reduce token usage. The agent writes code with quality standards in mind, but you manually run `pytest`, `ruff check`, and `mypy` for final validation.

**Best for:** Cost-conscious workflows or when you prefer manual control over validation timing.

Both files enforce the same code standards and project structure—only the automation scope differs.


## Features

- **Type hints**: Full type annotations for better IDE support and mypy compatibility
- **Pydantic validation**: Runtime type validation and serialization
- **Configuration**: Externalize settings using the `Config` class
- **Testing**: Comprehensive test suite with pytest
- **Code quality**: Automated linting with ruff and type checking with mypy
- **Security**: Dependency vulnerability scanning with pip-audit
- **Shell script linting**: Shell script validation with shellcheck for `*.sh` and `*.bash` files

## Python Best Practices Used

- ✅ **Type hints**: All functions and classes use type annotations
- ✅ **Docstrings**: Clear descriptions of modules, classes, and functions
- ✅ **Project structure**: Proper package layout with separation of concerns
- ✅ **Testing**: Comprehensive test coverage with pytest
- ✅ **Configuration**: Externalized config using pydantic BaseModel
- ✅ **Linting**: Code quality checks with ruff
- ✅ **Dependency management**: Explicit dependencies in pyproject.toml
- ✅ **Security**: Automated vulnerability scanning with pip-audit
- ✅ **Shell script quality**: Shell script linting with shellcheck
- ✅ **Python versions**: Supports Python 3.10+

## License

MIT

## Contributing

This is a template repository. Feel free to use it as a starting point for your own projects.

## Author

AlexAndrewsAI <alex.andrews.ai@protonmail.com>
