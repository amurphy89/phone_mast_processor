from datetime import datetime
from pprint import pprint

from . import csv_reader
from . import helpers
    
def phone_mast_info(file):

    earliest_date = datetime(1999, 6, 1)
    last_date = datetime(2007, 8, 31)
    data = csv_reader.read_csv(file)
    masts = helpers.map_data(data)

    masts_by_cheapest_rent = helpers.sort_by_current_rent(masts)
    masts_by_lease = helpers.filter_by_lease_years(masts, 25)
    total_rents = helpers.calculate_total_rent(masts)
    tenant_mast_map = helpers.group_masts_by_tenant(masts)
    masts_by_lease_date = helpers.filter_by_lease_start_date(
        masts,
        earliest_date,
        last_date
    )

    print('First 5 with lowest rent:\n')
    print_masts(masts_by_cheapest_rent)
    
    print('\nMasts with a lease of 25 years:\n')
    print_masts(masts_by_lease)

    print(f'\nThe total rent of all masts is: {round(total_rents, 2)}\n')
    
    print('\nTenant to mast mapping is as follows:\n')
    pprint(tenant_mast_map)

    print('\nAll rentals with a Lease Start Date between 1 June 1999 and 31 Aug 2007')
    print_masts(masts_by_lease_date)

def print_masts(masts):
    for mast in masts:
        print(mast)
