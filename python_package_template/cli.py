"""Command line interface module.

Provides a typer-based CLI for the package.
"""

import typer

from python_package_template.config import Config
from python_package_template.hello import HelloWorld

app = typer.Typer(help="Python package template CLI")


@app.command()
def hello(
    name: str = typer.Option("World",
        "--name", "-n",
        help="Name to greet (default: World)"
    ),
) -> None:
    """Greet the specified name.

    Args:
        name: The name to greet.
    """
    config = Config(name=name)
    hello_world = HelloWorld(config)
    greeting = hello_world.greet()
    typer.echo(greeting)

if __name__ == "__main__":
    app()
