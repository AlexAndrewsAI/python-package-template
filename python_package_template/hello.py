"""Hello world module.

Provides a simple greeting class that uses configuration.
"""

from python_package_template.config import Config


class HelloWorld:
    """A simple greeting class.

    Greets a name specified in the configuration.
    """

    def __init__(self, config: Config | None = None):
        """Initialize the HelloWorld instance.

        Args:
            config: Optional configuration object. If not provided,
                   a default Config instance will be created.
        """
        if config is None:
            config = Config()
        print(f"hello {config.name}")
