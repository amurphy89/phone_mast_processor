import csv


def read_csv(file):
    rows = []
    try:
        with open(file, "rt") as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                rows.append(row)
        if not rows:
            raise IOError
        return rows
    except FileNotFoundError:
        raise FileNotFoundError
