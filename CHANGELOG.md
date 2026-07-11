# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [0.1.1] - 2026-07-10 - #11 "Add python prek hooks for git pre-commit"

### Added

- Pre-commit hooks via prek with ruff, mypy, shellcheck, and standard pre-commit-hooks.
- `py.typed` marker for PEP 561 type stub compliance.
- CI matrix testing across Python 3.10–3.13.
- CI step to verify `CHANGELOG.md` is updated on pull requests.

### Changed

- `cli.py`: use `importlib.metadata.version()` instead of importing `__version__` from package root to avoid double-importing `__init__.py`.

## [0.1.0] - 2026-06-24 - #10 "avoid # type: ignore to fix mypy"

### Added

- `pip-audit` for automated dependency vulnerability scanning in CI.
- User-friendly error messages for invalid CLI input via Pydantic validation handling.

### Changed

- Enforced strict mypy compliance by removing `# type: ignore` comments.

## [0.0.3] - 2026-05-24 - #5 "template instructions added"

### Added

- `__main__.py` entry point enabling `python -m python_package_template` execution.
- `test_main_entry_point()` for 100% test coverage.

### Changed

- Updated license format to PEP 621 SPDX style (`license = "MIT"`).
- Replaced `pass` with `...` in the main CLI callback.

## [0.0.2] - 2026-05-23 - #4 "Feature/more support for agents"

### Added

- `AGENTS_MANUAL_CHECKS.md` for low-token agent workflows.
- Expanded `AGENTS.md` with comprehensive development guidelines.
- Stricter linting configuration (ruff, mypy).
- Centralized version management in `pyproject.toml`.

### Changed

- Updated dependencies (typer, typing-extensions, added typing-inspection).
- Fixed README usage examples to use `logging` instead of `print()`.

## [0.0.1] - 2026-05-17 - #2 "Feature/agents md"

### Added

- `AGENTS.md` with AI agent instructions for the project.

## 0.0.0 - 2026-05-09 - #1 "Cleanup and add cli"

### Added

- Initial project scaffold with Pydantic config, HelloWorld logic, and pytest suite.
