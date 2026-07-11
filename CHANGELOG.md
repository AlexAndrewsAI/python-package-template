# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [Unreleased]

## [0.1.0] - 2026-06-24

### Added

- `pip-audit` for automated dependency vulnerability scanning in CI.
- User-friendly error messages for invalid CLI input via Pydantic validation handling.

### Changed

- Enforced strict mypy compliance by removing `# type: ignore` comments.

## [0.0.3] - 2026-05-24

### Added

- `__main__.py` entry point enabling `python -m python_package_template` execution.
- `test_main_entry_point()` for 100% test coverage.

### Changed

- Updated license format to PEP 621 SPDX style (`license = "MIT"`).
- Replaced `pass` with `...` in the main CLI callback.

## [0.0.2] - 2026-05-23

### Added

- `AGENTS_MANUAL_CHECKS.md` for low-token AI agent workflows.
- Expanded `AGENTS.md` with comprehensive development guidelines.
- Stricter linting configuration (ruff, mypy).
- Centralized version management in `pyproject.toml`.

### Changed

- Updated dependencies (typer, typing-extensions, added typing-inspection).
- Fixed README usage examples to use `logging` instead of `print()`.

## [0.0.1] - 2026-05-17

### Added

- `AGENTS.md` with AI agent instructions for the project.

## 0.0.0 - 2026-05-01

### Added

- Initial project scaffold with Pydantic config, HelloWorld logic, and pytest suite.
