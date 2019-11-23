import click

from pprint import pprint

from . import csv_reader
from . import helpers

@click.command()
@click.argument('file')
def cli(file):
    data = csv_reader.read_csv(file)
    masts = helpers.map_data(data)

    masts_by_cheapest_rent = helpers.sort_by_current_rent(masts)
    masts_by_lease = helpers.filter_by_lease_years(masts, 25)
    total_rents = helpers.calculate_total_rent(masts)
    tenant_mast_map = helpers.group_masts_by_tenant(masts)

    print('First 5 with lowest rent:\n')
    print_masts(masts_by_cheapest_rent)
    
    print('Masts with a lease of 25 years:\n')
    print_masts(masts_by_lease)

    print(f'The total rent of all masts is: {round(total_rents, 2)}\n')
    
    print('Tenant to mast mapping is as follows:\n')
    pprint(tenant_mast_map)

def print_masts(masts):
    for mast in masts:
        print(mast)
    