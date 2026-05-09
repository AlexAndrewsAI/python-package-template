"""Tests for the hello module.
"""

import logging

from python_package_template import Config, HelloWorld


def test_default_name(caplog):
    """Test HelloWorld with default name.

    Args:
        caplog: Pytest fixture for capturing log output.
    """
    caplog.set_level(logging.INFO)
    HelloWorld()
    assert len(caplog.records) == 1
    assert caplog.records[0].message == "hello World"
    assert caplog.records[0].levelname == "INFO"


def test_custom_name(caplog):
    """Test HelloWorld with custom name.

    Args:
        caplog: Pytest fixture for capturing log output.
    """
    caplog.set_level(logging.INFO)
    HelloWorld(Config(name="Alice"))
    assert len(caplog.records) == 1
    assert caplog.records[0].message == "hello Alice"
    assert caplog.records[0].levelname == "INFO"
