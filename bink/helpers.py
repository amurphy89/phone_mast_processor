import itertools

from datetime import datetime

from .mast import Mast
from.levensthein import levenshtein_ratio_and_distance

def map_data(data):
    masts = []
    for row in data:
        masts.append(Mast(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10]))
    return masts

def sort_by_current_rent(masts):
    lowest_rents = masts
    lowest_rents.sort(key=lambda x: x.current_rent)
    return lowest_rents[:5]

def filter_by_lease_years(masts, years):
    return [x for x in masts if x.lease_years == years]

def calculate_total_rent(masts):
    return sum([x.current_rent for x in masts])

def group_masts_by_tenant(masts):
    result = {}

    for mast in masts:
        seen = False
        for tenant, count in result.items():
            ratio = round(levenshtein_ratio_and_distance(tenant, mast.tenant_name, ratio_calc=True), 2)
            is_similar = 0.62 <= ratio <= 1
            if is_similar:
                result[tenant] += 1
                seen = True
                break

        if seen:
            continue
        if mast.tenant_name not in result:
            result[mast.tenant_name] = 1

    return result

def filter_by_lease_start_date(masts, earliest_date, last_date):
    result = []
    for mast in masts:
        if earliest_date <= mast.lease_start_date <= last_date:
            result.append(mast)
    return result
