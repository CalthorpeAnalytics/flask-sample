import click
from flask.cli import with_appcontext


@click.group()
def cli() -> None:
    """Main entry point"""


@cli.command("init")
@with_appcontext
def init() -> None:
    """Initialize app for development"""
    click.echo("Initialized app for development")


if __name__ == "__main__":
    cli()
