import pandas

def read_csv(file):
    try:
        return pandas.read_csv(file)
    except FileNotFoundError:
        raise FileNotFoundError