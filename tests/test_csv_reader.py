import pandas
import pytest

from mock import patch
from pandas.errors import EmptyDataError

from bink import csv_reader

class TestBink:

    @patch('pandas.read_csv')
    def test_file_loads_and_returns_dataframe(self, mock_data_frame):
        mock_data_frame = pandas.DataFrame()
        result = csv_reader.read_csv('test.csv')

        assert result.values

    def test_file_not_found_raise_error(self):
        with pytest.raises(FileNotFoundError):
            csv_reader.read_csv('test.csv')
