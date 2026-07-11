"""Python package template.

A simple template for creating Python packages with configuration management
and a hello world example.
"""

from importlib.metadata import version

from python_package_template.config import DEFAULT_CONFIG, Config
from python_package_template.hello import HelloWorld

__version__ = version("python-package-template")
__all__ = ["DEFAULT_CONFIG", "Config", "HelloWorld", "__version__"]
