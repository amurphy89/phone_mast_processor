import click

from . import csv_reader

@click.command()
@click.argument(file)
def cli(file):
    try:
        data = csv_reader.read_csv(file)
    except FileNotFoundError:
        SystemExit("File was not found.")