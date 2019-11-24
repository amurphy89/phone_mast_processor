from datetime import datetime

from bink.mast import Mast

from bink import helpers


class TestHelpers:

    def setup(self):
        self.data = [
            ['Beecroft Hill', 'Broad Lane','','','LS13','Beecroft Hill - Telecom App','Arqiva Services ltd', '01 Mar 1994', '28 Feb 2058', '64', '4500.00'],
            ['Potternewton Crescent', 'Potternewton Est Playing Field','','','LS13','Beecroft Hill - Telecom App','Arqiva Services ltd', '01 Mar 1994', '28 Feb 2058', '10', '50000.00'],
            ['Potternewton Crescent', 'Potternewton Est Playing Field','','','LS13','Beecroft Hill - Telecom App','Arqiva Services ltd', '01 Mar 1994', '28 Feb 2058', '20', '60000.00'],
            ['Potternewton Crescent', 'Potternewton Est Playing Field','','','LS13','Beecroft Hill - Telecom App','Arqiva Services ltd', '01 Mar 1994', '28 Feb 2058', '30', '23950.00'],
            ['Potternewton Crescent', 'Potternewton Est Playing Field','','','LS13','Beecroft Hill - Telecom App','Arqiva Services ltd', '01 Mar 1994', '28 Feb 2058', '40', '23950.00'],
            ['Potternewton Crescent', 'Potternewton Est Playing Field','','','LS13','Beecroft Hill - Telecom App','Arqiva Services ltd', '01 Mar 1994', '28 Feb 2058', '50', '23950.00'],
        ]

        self.masts = [
            Mast('Beecroft Hill', 'Broad Lane','','','LS13','Beecroft Hill - Telecom App','EE', '01 Mar 2003', '28 Feb 2004', '64', '4500.00'),
            Mast('Potternewton Crescent', 'Potternewton Est Playing Field','','','LS13','Beecroft Hill - Telecom App','Arqiva Services Ltd', '01 Mar 1994', '28 Feb 2058', '10', '50000.00'),
            Mast('Potternewton Crescent', 'Potternewton Est Playing Field','','','LS13','Beecroft Hill - Telecom App','Arqiva Services ltd', '01 Mar 2000', '28 Feb 2058', '20', '60000.00'),
            Mast('Potternewton Crescent', 'Potternewton Est Playing Field','','','LS13','Beecroft Hill - Telecom App','Arqiva Services.', '01 Mar 2001', '28 Feb 2058', '30', '23950.00'),
            Mast('Potternewton Crescent', 'Potternewton Est Playing Field','','','LS13','Beecroft Hill - Telecom App','Arqiva Services ltd.', '01 Mar 2008', '28 Feb 2058', '40', '23950.00'),
            Mast('Potternewton Crescent', 'Potternewton Est Playing Field','','','LS13','Beecroft Hill - Telecom App','Vodafone', '01 Mar 1994', '28 Feb 2058', '64', '23950.00'),
            Mast('Potternewton Crescent', 'Potternewton Est Playing Field','','','LS13','Beecroft Hill - Telecom App','Vodafone Phones.', '01 Mar 1994', '28 Feb 2058', '64', '23950.00'),
        ]


    def test_map_data_returns_list_of_masts(self):
        result = helpers.map_data(self.data)

        assert isinstance(result[0], Mast)
        assert len(result) > 1

    def test_sort_by_current_rent_returns_in_ascending_order(self):
        result = helpers.sort_by_current_rent(self.masts)

        assert len(result) == 5
        assert result[0].current_rent == 4500.00
        assert result[4].current_rent == 23950.00

    def test_filter_by_lease_years_returns_filtered_list(self):
        result = helpers.filter_by_lease_years(self.masts, 64)

        assert result[0].lease_years == 64
        assert result[1].lease_years == 64

    def test_calculate_total_rent_returns_total_of_all_rents(self):
        result = helpers.calculate_total_rent(self.masts)

        assert result == 210300.00

    def test_group_masts_by_tenant(self):
        result = helpers.group_masts_by_tenant(self.masts)

        assert result['Arqiva Services Ltd'] == 4
        assert 'Arqiva Services.' not in result
        assert result['Vodafone'] == 2
        assert result['EE'] == 1

    def test_filter_by_lease_start_date(self):
        earliest_date = datetime(1999, 6, 1)
        last_date = datetime(2007, 8, 31)
        result = helpers.filter_by_lease_start_date(self.masts, earliest_date, last_date)
        
        assert len(result) == 3
