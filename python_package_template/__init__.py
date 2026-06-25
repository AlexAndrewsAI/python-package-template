"""Python package template.

A simple template for creating Python packages with configuration management
and a hello world example.
"""

from python_package_template.config import DEFAULT_CONFIG, Config
from python_package_template.hello import HelloWorld

__version__ = "0.1.1"
__all__ = ["DEFAULT_CONFIG", "Config", "HelloWorld"]
