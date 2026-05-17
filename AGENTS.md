# Agent Instructions: python-package-template

This project is a modern Python package template emphasizing best practices: `uv` for management, `pydantic` for validation, and `typer` for CLI.

## Tech Stack
- **Environment/Deps:** [uv](https://github.com/astral-sh/uv)
- **Validation:** [pydantic](https://docs.pydantic.dev/)
- **CLI:** [typer](https://typer.tiangolo.com/)
- **Testing:** [pytest](https://docs.pytest.org/)
- **Linting/Formatting:** [ruff](https://beta.ruff.rs/)
- **Type Checking:** [mypy](https://mypy.readthedocs.io/)

## Core Directives
- **Virtual Env:** ALWAYS use the `.venv` directory. Run `uv venv` if it's missing.
- **Python Invocation:** Prefer `python3` or `uv run python`.
- **Pathing:** NEVER use absolute paths. Always use relative paths from the repository root.
- **Isolation:** Do not access files outside the repository parent (`./..`) without explicit permission.
- **Interactivity:** Avoid commands that trigger interactive terminal prompts (e.g., `borg`, `keepass`). For testing, ensure these are mocked or bypassed.
- **Syncing:** Ensure the environment is synced before major operations: `uv sync --dev`.

## Workflow Commands
- **Setup:** `uv sync --dev`
- **Test:** `uv run pytest`
- **Lint:** `uv run ruff check .`
- **Format:** `uv run ruff format .`
- **Type Check:** `uv run mypy .`
- **CLI Dev:** `uv run python -m python_package_template.cli hello`

## Project Structure
- `python_package_template/`: Core logic.
    - `config.py`: Pydantic models for configuration.
    - `hello.py`: Core business logic (`HelloWorld` class).
    - `cli.py`: Typer-based CLI entry point.
- `tests/`: Pytest suite.
- `pyproject.toml`: Dependency and tool configuration.
