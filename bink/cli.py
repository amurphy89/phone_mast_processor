import click

from pprint import pprint as pp

from . import csv_reader
from . import helpers


@click.command()
@click.argument('file')
def cli(file):
    try:
        df = csv_reader.read_csv(file)
        print('Lowest 5 entries by Current Rent:\n')
        pp(helpers.sort_by_rent(df))
    except FileNotFoundError:
        SystemExit("File was not found.")

if __name__ == '__main__':
	cli()