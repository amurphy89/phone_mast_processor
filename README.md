#Phone Mast Data Processor

Load phone mast data, process and output to the console.

Installation
Install using pip:

```$ pip install phone_mast_processor```

or

```$ pipenv run pip install .```

##Usage

Usage: phone_mast_processor [OPTIONS] FILE

  This application processes phone mast data and outputs it to the console.

  The names of sections that can be run independently are:

  - rent - produces a list sorted by Current Rent in ascending order. years -
  - list of mast data where Lease Years = 25 years. 
  - total rent - the total
  - rent for all items. 
  - tenant - tenant name and a count of masts for each tenant. 
  - lease start date - data for rentals with Lease Start Date between 1 June 1999 and 31 Aug 2007.

  eg ```phone_mast_processor -s "total rent" data.csv```

##Development

Install pipenv and run from the base directory. This application has only been tested with Python 3.8 but will require at lease version 3.6 due to this use of f strings:

```pipenv install --dev```

Test

```pipenv run pytest```

Things to improve:

    - Comments!
    - Use the 'typing' library to support type hints e.g. def greeting(name: str) -> str:
    - Convince the Product Owner to allow me to use Pandas!
    - If the input file cannot be found or is empty, uses requests to download the file from the URL in the requirements.
    - Use OS lib to ensure the file path to data is correct cross platform.
