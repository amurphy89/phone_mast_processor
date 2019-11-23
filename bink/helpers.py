import pandas

def sort_by_rent(df):
    return df.sort_values(by=['Current Rent'])[:5]