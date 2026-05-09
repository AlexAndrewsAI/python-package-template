"""Tests for the hello module.
"""

from python_package_template import Config, HelloWorld


def test_default_name(capsys):
    """Test HelloWorld with default name.

    Args:
        capsys: Pytest fixture for capturing stdout/stderr.
    """
    HelloWorld()
    captured = capsys.readouterr()
    assert captured.out == "hello World\n"


def test_custom_name(capsys):
    """Test HelloWorld with custom name.

    Args:
        capsys: Pytest fixture for capturing stdout/stderr.
    """
    HelloWorld(Config(name="Alice"))
    captured = capsys.readouterr()
    assert captured.out == "hello Alice\n"
