from datetime import datetime
from pprint import pprint

from . import csv_reader
from . import helpers


class PhoneMastInfo:

    def __init__(self, section, file):
        data = csv_reader.read_csv(file)
        self.section = section
        self.masts = helpers.map_data(data)

    def display_phone_mast_info(self):

        sections = {
            'rent': PhoneMastInfo.masts_by_cheapest_rent,
            'years': PhoneMastInfo.masts_by_lease,
            'total rent': PhoneMastInfo.total_rents,
            'tenant': PhoneMastInfo.tenant_mast_map,
            'lease start date': PhoneMastInfo.masts_by_lease_start_date,
        }

        if not self.section:
            for func in sections.values():
                func(self.masts)
        else:
            func = sections[self.section]
            func(self.masts)

    @staticmethod
    def print_masts(masts):
        for mast in masts:
            print(mast)

    @staticmethod
    def masts_by_cheapest_rent(masts):
        masts_by_cheapest_rent = helpers.sort_by_current_rent(masts)
        print("First 5 with lowest rent:\n")
        PhoneMastInfo.print_masts(masts_by_cheapest_rent)

    @staticmethod
    def masts_by_lease(masts):
        masts_by_lease = helpers.filter_by_lease_years(masts, 25)
        print("\nMasts with a lease of 25 years:\n")
        PhoneMastInfo.print_masts(masts_by_lease)

    @staticmethod
    def total_rents(masts):
        total_rents = helpers.calculate_total_rent(masts)
        print(f"\nThe total rent of all masts is: {round(total_rents, 2)}\n")

    @staticmethod
    def tenant_mast_map(masts):
        tenant_mast_map = helpers.group_masts_by_tenant(masts)
        print("\nTenant to mast mapping is as follows:\n")
        pprint(tenant_mast_map)
    
    @staticmethod
    def masts_by_lease_start_date(masts):
        earliest_date = datetime(1999, 6, 1)
        last_date = datetime(2007, 8, 31)
        masts_by_lease_date = helpers.filter_by_lease_start_date(
            masts,
            earliest_date,
            last_date
        )

        print("\nAll rentals with a Lease Start Date between 1 June 1999 and 31 Aug 2007")
        PhoneMastInfo.print_masts(masts_by_lease_date)


