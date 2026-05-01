from python_package_template.config import Config


class HelloWorld:
    def __init__(self, config: Config | None = None):
        if config is None:
            config = Config()
        print(f"hello {config.name}")
