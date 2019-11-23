import pandas

from bink import helpers

class TestHelpers:

    def test_sort_by_rent_returns_five_items_with_lowest_rent(self):
        rent_data = ['1', '2', '3', '4', '5', '6']
        df = pandas.DataFrame(rent_data, columns=['Current Rent'])
        result = helpers.sort_by_rent(df)
        assert len(result)
        assert '6' not in result