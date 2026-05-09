# python-package-template

A basic template package demonstrating Python packaging best practices using **uv**, **pydantic**, and **pytest**.

## Overview

This is a minimal but well-structured Python package that serves as a template for building larger projects. It demonstrates:

- Modern Python packaging with `pyproject.toml`
- Type hints and static type checking with **mypy**
- Data validation using **pydantic**
- Code linting with **ruff**
- Testing with **pytest**
- Dependency management with **uv**

This package is intentionally simple to provide a clean starting point for your own projects.

## Installation

### Prerequisites

- Python 3.10 or higher
- [uv](https://github.com/astral-sh/uv) package manager

### Setup

Clone the repository and install dependencies:

```bash
git clone https://github.com/AlexAndrewsAI/python-package-template.git
cd python-package-template  
uv sync
```

## Usage

### Basic Example

```python
from python_package_template.hello import HelloWorld
from python_package_template.config import Config

# Create with default name
hello = HelloWorld()
print(hello.greet())  # Output: Hello, World!

# Create with custom name
hello = HelloWorld(Config(name="Alice"))
print(hello.greet())  # Output: Hello, Alice!
```

### Configuration

The `Config` class uses **pydantic** for validation:

```python
from python_package_template.config import Config

# Create with default name
config = Config()

# Create with custom name
config = Config(name="Alice")

# Access the name
print(config.name)  # Output: Alice
```

### Command Line Interface

The package includes a CLI tool built with **typer**:

```bash
# Run the CLI with default name
uv run python -m python_package_template.cli hello

# Greet a specific name
uv run python -m python_package_template.cli hello --name Alice

# Show help
uv run python -m python_package_template.cli hello --help
```

The CLI supports the following options:
- `--name, -n TEXT`: Name to greet (default: World)
- `--help, -h`: Show help message

## Development

### Install Dev Dependencies

```bash
uv sync
```

This installs all dependencies and dev tools (pytest, ruff, mypy).

### Run Tests

```bash
# Run all tests
uv run pytest

# Run with verbose output
uv run pytest -v

# Run specific test
uv run pytest tests/test_hello.py::test_default_name

# Show print statements during tests
uv run pytest -s
```

### Code Quality

```bash
# Lint code
uv run ruff check python_package_template tests

# Type check
uv run mypy python_package_template
```

## Project Structure

```
python-package-template/
├── .gitignore
├── pyproject.toml
├── README.md
├── python_package_template/
│   ├── __init__.py
│   ├── cli.py
│   ├── config.py
│   └── hello.py
└── tests/
    ├── __init__.py
    └── test_hello.py

```

## Features

- **Type hints**: Full type annotations for better IDE support and mypy compatibility
- **Pydantic validation**: Runtime type validation and serialization
- **Configuration**: Externalize settings using the `Config` class
- **Testing**: Comprehensive test suite with pytest
- **Code quality**: Automated linting with ruff and type checking with mypy

## Python Best Practices Used

- ✅ **Type hints**: All functions and classes use type annotations
- ✅ **Docstrings**: Clear descriptions of modules, classes, and functions
- ✅ **Project structure**: Proper package layout with separation of concerns
- ✅ **Testing**: Comprehensive test coverage with pytest
- ✅ **Configuration**: Externalized config using pydantic BaseModel
- ✅ **Linting**: Code quality checks with ruff
- ✅ **Dependency management**: Explicit dependencies in pyproject.toml
- ✅ **Python versions**: Supports Python 3.8+

## License

MIT

## Contributing

This is a template repository. Feel free to use it as a starting point for your own projects.

## Author

AlexAndrewsAI <alex.andrews.ai@protonmail.com>