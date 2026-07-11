"""Hello world module.

Provides a simple greeting class that uses configuration.
"""

import logging

from python_package_template.config import DEFAULT_CONFIG, Config

logger = logging.getLogger(__name__)


class HelloWorld:
    """A simple greeting class.

    Greets a name specified in the configuration.
    """

    def __init__(self, config: Config | None = None) -> None:
        """Initialize the HelloWorld instance.

        Args:
            config: Optional configuration object. If not provided,
                   the default singleton config will be used.

        """
        if config is None:
            config = DEFAULT_CONFIG
        self.config = config

    def greet(self) -> str:
        """Generate a greeting message.

        Returns:
            A greeting string with the configured name.

        """
        logger.info("hello %s", self.config.name)
        return f"Hello, {self.config.name}!"
