# Checks that the JSON and generated Excel files contain matching purchase test data.
from utils.data_reader import read_excel, read_json


def test_json_and_excel_purchase_data_are_consistent():
    """Verifies both required data sources and creates the Excel seed on a fresh clone."""
    json_data = read_json()
    excel_data = read_excel()

    assert excel_data["product"] == json_data["product"]
    assert excel_data["quantity"] == json_data["quantity"]
    assert excel_data["currency"] == json_data["currency"]
