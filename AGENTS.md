# Agent Instructions: python-package-template

## Tech Stack
- **Environment/Deps:** uv
- **Validation:** pydantic
- **CLI:** typer
- **Testing:** pytest
- **Linting/Formatting:** ruff
- **Type Checking:** mypy

## Core Directives
- **Self-Maintenance:** Keep this file current. Update "Tech Stack", "Workflow Commands", and "Project Structure" if you modify `pyproject.toml`, project structure, or core logic.
- **Virtual Env:** Activate `.venv`. Run `uv venv` if missing.
- **Python Invocation:** Prefer `python3` or `uv run python`.
- **Relative Paths Only:** Never use absolute paths.
- **Type Hints:** ALL function signatures and class members require type hints. Strict mypy enforcement.
- **Logging:** Use `logging`, never `print()`.
- **Dependencies:** Use `uv add`/`uv remove`. Don't edit `pyproject.toml` manually.
- **Testing:** Every code change requires tests in `tests/`. Ensure `uv run pytest` passes.
- **Docstrings:** Google-style for all public APIs.
- **No Interactive Prompts:** Mock or bypass interactive commands.
- **No Git Operations:** Don't stage/commit unless explicitly requested.
- **Code Reviews:** Analyze only, record findings in `./REVIEW.md`, no modifications.
- **Pre-Operation Sync:** Run `uv sync --dev` before major work.

## Workflow Commands
- **Setup:** `uv sync --dev`
- **Test:** `uv run pytest`
- **Lint:** `uv run ruff check .`
- **Format:** `uv run ruff format .`
- **Type Check:** `uv run mypy .`
- **CLI Dev:** `uv run python -m python_package_template.cli hello`

## Project Structure
- `python_package_template/`: Core logic
  - `config.py`: Pydantic models
  - `hello.py`: Business logic
  - `cli.py`: Typer CLI
- `tests/`: Pytest suite
- `pyproject.toml`: Dependencies & tools
