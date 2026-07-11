# Agent Instructions: python-package-template (Manual Checks)

## Quick Start
1. **Setup:** Run `uv sync --dev` before major work sessions
2. **Activate:** Ensure `.venv` is active; run `uv venv` if missing
3. **Code:** Use `python3` or `uv run python`; always add type hints and tests

## Tech Stack
| Component | Tool |
|-----------|------|
| Environment & Dependencies | uv |
| Data Validation | Pydantic |
| CLI Framework | Typer |
| Testing | pytest |
| Linting & Formatting | ruff |
| Type Checking | mypy |
| Security Audit | pip-audit |
| Git Hooks | prek |

## Project Structure
```
python_package_template/
  ├── config.py          (Pydantic models)
  ├── hello.py           (Business logic)
  └── cli.py             (Typer CLI)
tests/                   (Pytest suite)
pyproject.toml           (Dependencies & tool config)
.pre-commit-config.yaml  # Pre-commit hooks configuration
```

## Essential Directives

### Code Standards
- **Type Hints:** Required on ALL function signatures and class members. Avoid using `# type: ignore` comments to suppress mypy errors; fix the underlying type issues instead.
- **Docstrings:** Google-style format for all public APIs.
- **Logging:** Use `logging` module only; never `print()`.
- **Relative Paths:** Never use absolute paths in code.

### Dependency & Configuration Management
- **Adding/Removing Dependencies:** Use `uv add` / `uv remove` commands.
- **Editing pyproject.toml:** Avoid manual edits during development. Only update `pyproject.toml` as the **final change** after all work is tested and finalized.
- **Before Major Work:** Always run `uv sync --dev` first.

### Testing & Quality
- **Test Coverage:** Every code change requires corresponding tests in `tests/`.
- **Validation:** You do NOT run validation tools. Write code with quality standards in mind (type hints, docstrings, tests). The user will run `pytest`, `ruff check`, `ruff format`, and `mypy` manually for final validation.

### Operational Constraints
- **No Interactive Prompts:** Mock or bypass any interactive commands.
- **Staging & Commit Protocol:** When you have completed work and updated files, stage the changes with `git add` and then display a suggested commit message for the user's review. DO NOT actually commit - only stage and display the message.
- **Code Review Mode:** Analyze only; record findings in `./REVIEW.md` without making modifications. At the top of the review, identify the reviewer including the name of the IDE/CLI used and the primary model that performed the review.

### File Maintenance
- **Keep Instructions Current:** Update "Tech Stack," "Project Structure," and "Workflow Commands" if `pyproject.toml`, structure, or core logic changes.

## Workflow Commands
```bash
uv sync --dev                           # Install/sync all dependencies
uv run hello-world hello                # Test CLI
```
