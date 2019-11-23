from .mast import Mast

def map_data(data):
    masts = []
    for row in data:
        masts.append(Mast(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10]))
    return masts

def sort_by_current_rent(masts):
    lowest_rents = masts
    lowest_rents.sort(key=lambda x: float(x.current_rent))
    return lowest_rents[:5]

