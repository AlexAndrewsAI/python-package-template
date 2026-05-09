"""Command line interface module.

Provides a typer-based CLI for the package.
"""

import typer

from python_package_template.config import Config
from python_package_template.hello import HelloWorld

app = typer.Typer(help="Python package template CLI")


@app.command()
def hello(
    name: str = typer.Option("World", "--name", help="Name to greet (default: World)"),
    help_flag: bool = typer.Option(False, "--help", "-h", help="Show help message"),
) -> None:
    """Greet the specified name.

    Args:
        name: The name to greet.
        help_flag: Show help message.
    """
    if help_flag:
        typer.echo("Usage: python -m python_package_template.cli hello")
        typer.echo("\nOptions:")
        typer.echo("  --name, -n TEXT    Name to greet (default: World)")
        typer.echo("  --help, -h         Show this help message")
        return

    config = Config(name=name)
    HelloWorld(config)
    typer.echo(f"Hello, {name}!")


if __name__ == "__main__":
    app()
