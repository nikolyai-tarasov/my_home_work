import unittest
from unittest.mock import patch
from src.external_api import currency_conversion, read_file


@patch("requests.request")
def test_currency_conversion(mock_get):
    mock_get.return_value.json.return_value = {"operationAmount": {"amount": "31957.58"}}
    assert currency_conversion(read_file("../data/tests_operations.json")) == 2800296.753175
    mock_get.assert_called_once_with(
        "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount="
    )


if __name__ == "__main__":
    unittest.main()
