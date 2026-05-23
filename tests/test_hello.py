"""Tests for the hello module."""

import logging

import pytest
from typer.testing import CliRunner

from python_package_template import Config, HelloWorld
from python_package_template.cli import app


def test_default_name(caplog: pytest.LogCaptureFixture) -> None:
    """Test HelloWorld with default name.

    Args:
        caplog: Pytest fixture for capturing log output.
    """
    caplog.set_level(logging.INFO)
    hello_world = HelloWorld()
    greeting = hello_world.greet()
    assert greeting == "Hello, World!"
    assert len(caplog.records) == 1
    assert caplog.records[0].message == "hello World"
    assert caplog.records[0].levelname == "INFO"


def test_custom_name(caplog: pytest.LogCaptureFixture) -> None:
    """Test HelloWorld with custom name.

    Args:
        caplog: Pytest fixture for capturing log output.
    """
    caplog.set_level(logging.INFO)
    hello_world = HelloWorld(Config(name="Alice"))
    greeting = hello_world.greet()
    assert greeting == "Hello, Alice!"
    assert len(caplog.records) == 1
    assert caplog.records[0].message == "hello Alice"
    assert caplog.records[0].levelname == "INFO"


# CLI Tests
runner = CliRunner()


def test_cli_hello_default() -> None:
    """Test CLI hello command with default name."""
    result = runner.invoke(app, ["hello"])
    assert result.exit_code == 0
    assert "Hello, World!" in result.output


def test_cli_hello_custom_name() -> None:
    """Test CLI hello command with custom name."""
    result = runner.invoke(app, ["hello", "--name", "Alice"])
    assert result.exit_code == 0
    assert "Hello, Alice!" in result.output


def test_cli_hello_short_option() -> None:
    """Test CLI hello command with short option."""
    result = runner.invoke(app, ["hello", "-n", "Bob"])
    assert result.exit_code == 0
    assert "Hello, Bob!" in result.output


def test_cli_version() -> None:
    """Test CLI --version flag."""
    result = runner.invoke(app, ["--version"])
    assert result.exit_code == 0
    assert "python-package-template version:" in result.output


def test_cli_version_short() -> None:
    """Test CLI -V short flag."""
    result = runner.invoke(app, ["-V"])
    assert result.exit_code == 0
    assert "python-package-template version:" in result.output


def test_cli_hello_version() -> None:
    """Test CLI hello subcommand --version flag."""
    result = runner.invoke(app, ["hello", "--version"])
    assert result.exit_code == 0
    assert "python-package-template version:" in result.output


def test_cli_hello_empty_name() -> None:
    """Test CLI hello command with empty string name."""
    result = runner.invoke(app, ["hello", "--name", ""])
    assert result.exit_code == 0
    assert "Hello, !" in result.output
