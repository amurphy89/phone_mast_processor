import sys

import click

from .phone_mast_info import phone_mast_info

@click.command()
@click.argument('file')
def cli(file):
    try:
        phone_mast_info(file)
    except FileNotFoundError:
        sys.exit("The input file could not be found.")
    except IOError:
        sys.exit("The input file is empty or corrupt.")
    except Exception as e:
        sys.exit(f"The following error occurred: {e}")

if __name__ == '__main__':
	cli()