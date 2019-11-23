import pandas

def read_csv(file):
    try:
        csv = pandas.read_csv(file)
    except FileNotFoundError:
        raise FileNotFoundError