import unittest
from unittest.mock import patch
from src.external_api import currency_conversion, read_file


@patch("requests.request")
def test_currency_conversion(mock_get):
    mock_get.return_value.json.return_value = {"result": 2780295.878029}
    assert currency_conversion(read_file("../data/data_json/tests_operations.json")) == 2780295.878029
    mock_get.assert_called_once_with(
        "GET",
        "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=31957.58",
        headers={"apikey": "GOPnsVnjeGo3YO9JctoMd6ZfA4rjYTBW"},
        data={},
    )


if __name__ == "__main__":
    unittest.main()
