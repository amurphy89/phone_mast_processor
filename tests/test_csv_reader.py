from mock import mock_open, patch

from bink import csv_reader

class TestBink:
    
    def setup(self):
        self.csv = csv = '''col1,col2\ntest1,test2\ntest3,test4'''

    def test_file_loads_and_returns_data_in_list(self):
        m = mock_open()
        with patch('bink.csv_reader.open', mock_open(read_data=self.csv), create=True) as m:
            result = csv_reader.read_csv('test.csv')

        m.assert_called_once_with('test.csv', 'rt')
        print(f"result: {result}")
        assert result == [['test1', 'test2'], ['test3', 'test4']]

