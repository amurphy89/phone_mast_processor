import csv


def read_csv(file):
    rows = []
    try:
        with open(file, 'rt') as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                rows.append(row)
        return rows
    except FileNotFoundError:
        raise FileNotFoundError
    except IOError:
        raise IOError