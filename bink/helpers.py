
def sort_by_rent(df):
    sorted_by_rent = df.sort_values(by=['Current Rent'])[:5]
    return sorted_by_rent.values.tolist()