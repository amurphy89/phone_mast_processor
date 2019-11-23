from shutil import rmtree

from setuptools import find_packages, setup, Command

# Package meta-data.
NAME = 'bink'
DESCRIPTION = 'Load phone mast data, process and output to console.'
URL = 'https://github.com/amurphy9956/bink'
EMAIL = 'amurphy9956@live.com'
AUTHOR = 'Ashley Murphy'
REQUIRES_PYTHON = '>=3.7.0'
VERSION = '0.1.0'

# Required packages.
REQUIRED = ['click', 'requests']

# Optional packages.
EXTRAS = {}

setup(
    name=NAME, # Replace with your own username
    version=VERSION,
    author=AUTHOR,
    author_email=EMAIL,
    description=DESCRIPTION,
    entry_points={
        'console_scripts': ['bink=bink.cli:cli'],
    },
    url=URL,
    packages=find_packages(exclude=['tests', '*.tests', '*.tests.*', 'tests.*']),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires=REQUIRES_PYTHON,
    extras_require=EXTRAS,
    include_package_data=True,
    license='MIT'
)