import pytest

from mock import mock_open, patch

from phone_mast_processor import csv_reader

class Testphone_mast_processor:
    
    def setup(self):
        self.csv = csv = '''col1,col2\ntest1,test2\ntest3,test4'''

    def test_file_loads_and_returns_data_in_list(self):
        with patch('phone_mast_processor.csv_reader.open', mock_open(read_data=self.csv), create=True) as m:
            result = csv_reader.read_csv('test.csv')

        m.assert_called_once_with('test.csv', 'rt')
        print(f"result: {result}")
        assert result == [['test1', 'test2'], ['test3', 'test4']]

    def test_file_not_found_raise_error(self):
        with pytest.raises(FileNotFoundError):
            csv_reader.read_csv('test.csv')

    def test_file_corrupt_raise_error(self):
        with pytest.raises(IOError):
            with patch('phone_mast_processor.csv_reader.open', mock_open(read_data='\tgjhkh'), create=True) as m:
                result = csv_reader.read_csv('test.csv')
                assert result == 1
