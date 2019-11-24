import pytest

from phone_mast_processor.mast import Mast

@pytest.fixture
def data():
    return [
            ['Beecroft Hill', 'Broad Lane','','','LS13','Beecroft Hill - Telecom App','Arqiva Services ltd', '01 Mar 1994', '28 Feb 2058', '64', '4500.00'],
            ['Potternewton Crescent', 'Potternewton Est Playing Field','','','LS13','Beecroft Hill - Telecom App','Arqiva Services ltd', '01 Mar 1994', '28 Feb 2058', '10', '50000.00'],
            ['Potternewton Crescent', 'Potternewton Est Playing Field','','','LS13','Beecroft Hill - Telecom App','Arqiva Services ltd', '01 Mar 1994', '28 Feb 2058', '20', '60000.00'],
            ['Potternewton Crescent', 'Potternewton Est Playing Field','','','LS13','Beecroft Hill - Telecom App','Arqiva Services ltd', '01 Mar 1994', '28 Feb 2058', '30', '23950.00'],
            ['Potternewton Crescent', 'Potternewton Est Playing Field','','','LS13','Beecroft Hill - Telecom App','Arqiva Services ltd', '01 Mar 1994', '28 Feb 2058', '40', '23950.00'],
            ['Potternewton Crescent', 'Potternewton Est Playing Field','','','LS13','Beecroft Hill - Telecom App','Arqiva Services ltd', '01 Mar 1994', '28 Feb 2058', '50', '23950.00'],
        ]

@pytest.fixture
def masts():
    return [
        Mast('Beecroft Hill', 'Broad Lane','','','LS13','Beecroft Hill - Telecom App','EE', '01 Mar 2003', '28 Feb 2004', '64', '4500.00'),
        Mast('Potternewton Crescent', 'Potternewton Est Playing Field','','','LS13','Beecroft Hill - Telecom App','Arqiva Services Ltd', '01 Mar 1994', '28 Feb 2058', '10', '50000.00'),
        Mast('Potternewton Crescent', 'Potternewton Est Playing Field','','','LS13','Beecroft Hill - Telecom App','Arqiva Services ltd', '01 Mar 2000', '28 Feb 2058', '20', '60000.00'),
        Mast('Potternewton Crescent', 'Potternewton Est Playing Field','','','LS13','Beecroft Hill - Telecom App','Arqiva Services.', '01 Mar 2001', '28 Feb 2058', '30', '23950.00'),
        Mast('Potternewton Crescent', 'Potternewton Est Playing Field','','','LS13','Beecroft Hill - Telecom App','Arqiva Services ltd.', '01 Mar 2008', '28 Feb 2058', '40', '23950.00'),
        Mast('Potternewton Crescent', 'Potternewton Est Playing Field','','','LS13','Beecroft Hill - Telecom App','Vodafone', '01 Mar 1994', '28 Feb 2058', '64', '23950.00'),
        Mast('Potternewton Crescent', 'Potternewton Est Playing Field','','','LS13','Beecroft Hill - Telecom App','Vodafone Phones.', '01 Mar 1994', '28 Feb 2058', '64', '23950.00'),
    ]