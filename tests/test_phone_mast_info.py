import io
import sys
import pytest

from mock import patch

from phone_mast_processor.phone_mast_info import PhoneMastInfo

from .test_fixtures import data

class TestPhoneMastInfo:

    def setup(self):
        self.captured_output = io.StringIO()
        sys.stdout = self.captured_output

    def teardown(self):
        sys.stdout = sys.__stdout__

    @patch("phone_mast_processor.phone_mast_info.csv_reader.read_csv")
    def test_no_defined_section_runs_all_sections(self, mock_csv_reader, data):
        mock_csv_reader.return_value = data

        PhoneMastInfo("", "").display_phone_mast_info()       
        captured_output = self.captured_output.getvalue()

        assert "First 5 with lowest rent:" in captured_output
        assert "Masts with a lease of 25 years:" in captured_output
        assert "The total rent of all masts is:" in captured_output
        assert "Tenant to mast mapping is as follows:" in captured_output
        assert "All rentals with a Lease Start Date between 1 June 1999 and 31 Aug 2007" in captured_output

    @pytest.mark.parametrize("section, expected",
     [
        ("rent", "First 5 with lowest rent:"),
        ("years", "Masts with a lease of 25 years:"),
        ("total rent", "The total rent of all masts is:"),
        ("tenant", "Tenant to mast mapping is as follows:"),
        ("lease start date", "All rentals with a Lease Start Date between 1 June 1999 and 31 Aug 2007")
     ]
    )
    @patch("phone_mast_processor.phone_mast_info.csv_reader.read_csv")
    def test_section_years_runs_masts_by_lease(self, mock_csv_reader, data, section, expected, ):
        mock_csv_reader.return_value = data

        PhoneMastInfo(section, "").display_phone_mast_info()

        assert expected in self.captured_output.getvalue()
