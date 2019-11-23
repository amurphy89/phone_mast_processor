import click


@click.command()
@click.argument(file)
def cli(file):
    