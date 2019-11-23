from bink.mast import Mast

from bink import helpers


class TestHelpers:

    def setup(self):
        self.data = [
            ['Beecroft Hill', 'Broad Lane','','','LS13','Beecroft Hill - Telecom App','Arqiva Services ltd', '01 Mar 1994', '28 Feb 2058', '64', '4500.00'],
            ['Potternewton Crescent', 'Potternewton Est Playing Field','','','LS13','Beecroft Hill - Telecom App','Arqiva Services ltd', '01 Mar 1994', '28 Feb 2058', '64', '50000.00'],
            ['Potternewton Crescent', 'Potternewton Est Playing Field','','','LS13','Beecroft Hill - Telecom App','Arqiva Services ltd', '01 Mar 1994', '28 Feb 2058', '64', '60000.00'],
            ['Potternewton Crescent', 'Potternewton Est Playing Field','','','LS13','Beecroft Hill - Telecom App','Arqiva Services ltd', '01 Mar 1994', '28 Feb 2058', '64', '23950.00'],
            ['Potternewton Crescent', 'Potternewton Est Playing Field','','','LS13','Beecroft Hill - Telecom App','Arqiva Services ltd', '01 Mar 1994', '28 Feb 2058', '64', '23950.00'],
            ['Potternewton Crescent', 'Potternewton Est Playing Field','','','LS13','Beecroft Hill - Telecom App','Arqiva Services ltd', '01 Mar 1994', '28 Feb 2058', '64', '23950.00'],
        ]

        self.masts = [
            Mast('Beecroft Hill', 'Broad Lane','','','LS13','Beecroft Hill - Telecom App','Arqiva Services ltd', '01 Mar 1994', '28 Feb 2058', '64', '4500.00'),
            Mast('Potternewton Crescent', 'Potternewton Est Playing Field','','','LS13','Beecroft Hill - Telecom App','Arqiva Services ltd', '01 Mar 1994', '28 Feb 2058', '64', '50000.00'),
            Mast('Potternewton Crescent', 'Potternewton Est Playing Field','','','LS13','Beecroft Hill - Telecom App','Arqiva Services ltd', '01 Mar 1994', '28 Feb 2058', '64', '60000.00'),
            Mast('Potternewton Crescent', 'Potternewton Est Playing Field','','','LS13','Beecroft Hill - Telecom App','Arqiva Services ltd', '01 Mar 1994', '28 Feb 2058', '64', '23950.00'),
            Mast('Potternewton Crescent', 'Potternewton Est Playing Field','','','LS13','Beecroft Hill - Telecom App','Arqiva Services ltd', '01 Mar 1994', '28 Feb 2058', '64', '23950.00'),
            Mast('Potternewton Crescent', 'Potternewton Est Playing Field','','','LS13','Beecroft Hill - Telecom App','Arqiva Services ltd', '01 Mar 1994', '28 Feb 2058', '64', '23950.00'),
        ]


    def test_map_data_returns_list_of_masts(self):
        result = helpers.map_data(self.data)

        assert isinstance(result[0], Mast)
        assert len(result) > 1

    def test_sort_by_current_rent_returns_in_ascending_order(self):
        result = helpers.sort_by_current_rent(self.masts)

        assert len(result) == 5
        assert result[0].current_rent == '4500.00'
        assert result[4].current_rent == '50000.00'

        
