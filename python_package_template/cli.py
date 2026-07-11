"""Command line interface module.

Provides a typer-based CLI for the package.
"""

import logging

import typer
from pydantic import ValidationError

from python_package_template import __version__
from python_package_template.config import DEFAULT_CONFIG, Config
from python_package_template.hello import HelloWorld

logger = logging.getLogger(__name__)

__all__ = ["app"]

app = typer.Typer(help="Python package template CLI")


def version_callback(value: bool) -> None:
    """Handle the version flag callback."""
    if value:
        typer.echo(f"python-package-template version: {__version__}")
        raise typer.Exit()


@app.callback()
def main(
    version: bool | None = typer.Option(
        None,
        "--version",
        "-V",
        callback=version_callback,
        is_eager=True,
        help="Show the version and exit.",
    ),
) -> None:
    """Python package template CLI."""
    ...


@app.command()
def hello(
    name: str = typer.Option(
        "World", "--name", "-n", help="Name to greet (default: World)"
    ),
) -> None:
    """Greet the specified name.

    Args:
        name: The name to greet.

    """
    try:
        config = DEFAULT_CONFIG if name == "World" else Config(name=name)
    except ValidationError as e:
        logger.debug("Validation error: %s", e)
        typer.echo(f"Error: Invalid input - {e}", err=True)
        raise typer.Exit(code=1) from None
    hello_world = HelloWorld(config)
    greeting = hello_world.greet()
    typer.echo(greeting)


if __name__ == "__main__":
    app()
