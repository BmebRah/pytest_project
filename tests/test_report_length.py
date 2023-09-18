from lib.report_length import *

def test_report_length():
    result = report_length('tests')
    assert result == f"This string was 5 characters long."   

