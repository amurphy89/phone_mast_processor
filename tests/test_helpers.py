from datetime import datetime

from phone_mast_processor.mast import Mast

from phone_mast_processor import helpers

from .test_fixtures import data, masts


class TestHelpers:

    def test_map_data_returns_list_of_masts(self, data):
        result = helpers.map_data(data)

        assert isinstance(result[0], Mast)
        assert len(result) > 1

    def test_sort_by_current_rent_returns_in_ascending_order(self, masts):
        result = helpers.sort_by_current_rent(masts)

        assert len(result) == 5
        assert result[0].current_rent == 4500.00
        assert result[4].current_rent == 23950.00

    def test_filter_by_lease_years_returns_filtered_list(self, masts):
        result = helpers.filter_by_lease_years(masts, 64)

        assert result[0].lease_years == 64
        assert result[1].lease_years == 64

    def test_calculate_total_rent_returns_total_of_all_rents(self, masts):
        result = helpers.calculate_total_rent(masts)

        assert result == 210300.00

    def test_group_masts_by_tenant(self, masts):
        result = helpers.group_masts_by_tenant(masts)

        assert result['Arqiva Services Ltd'] == 4
        assert 'Arqiva Services.' not in result
        assert result['Vodafone'] == 2
        assert result['EE'] == 1

    def test_filter_by_lease_start_date(self, masts):
        earliest_date = datetime(1999, 6, 1)
        last_date = datetime(2007, 8, 31)
        result = helpers.filter_by_lease_start_date(masts, earliest_date, last_date)
        
        assert len(result) == 3
