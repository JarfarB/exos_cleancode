import logging

import click

"""logfile = Path(__file__).parent / "hello.log"
logger = logging.getLogger("hello_log")
logger.setLevel(logging.INFO)
file = logging.FileHandler(logfile, encoding="utf-8")
file.setLevel(logging.INFO)


file_format = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file.setFormatter(file_format)"""


@click.command()
@click.option(
    "--name",
    help="The person to greet.",
)
def hello(name):
    """Say hello to NAME."""
    click.echo(f"Hello {name}!")
    logger.log(logging.INFO, "✅ Hello executed.")


if __name__ == "__main__":
    hello()
