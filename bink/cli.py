import click

from pprint import pprint

from . import csv_reader
from . import helpers

@click.command()
@click.argument('file')
def cli(file):
    pass
    data = csv_reader.read_csv(file)
    masts = helpers.map_data(data)

    cheapest_masts_by_rent = helpers.sort_by_current_rent(masts)


    print("First 5 with lowest rent\n")
    for mast in cheapest_masts_by_rent:
        pprint(mast.to_dict())
    