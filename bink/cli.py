import sys

import click

from .phone_mast_info import PhoneMastInfo

@click.command()
@click.option("--section", "-s", default=None, help="Choose a single section to run.")
@click.argument("file")
def cli(section, file):
    """
    This application processes phone mast data and outputs it to the console.

    The names of sections that can be run independently are:

    rent - produces a list sorted by Current Rent in ascending order.
    years - list of mast data where Lease Years = 25 years.
    total rent - the total rent for all items.
    tenant - tenant name and a count of masts for each tenant.
    lease start date - data for rentals with Lease Start Date between 1 June 1999 and 31 Aug 2007.
    """
    try:
        phone_mast_info = PhoneMastInfo(section, file)
        phone_mast_info.display_phone_mast_info()
    except FileNotFoundError:
        sys.exit("The input file could not be found.")
    except IOError:
        sys.exit("The input file is empty or corrupt.")
    except Exception as e:
        sys.exit(f"The following error occurred: {e}")

if __name__ == "__main__":
	cli()