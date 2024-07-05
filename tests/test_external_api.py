import unittest
from unittest.mock import patch
from src.external_api import currency_conversion


class TestCurrencyConversion(unittest.TestCase):
    @patch("src.external_api.requests.get")
    def test_currency_conversion(self, mock_get):
        # Настройка mock-объекта
        mock_get.return_value.json.return_value = {"result": 75.0}
        transaction = {"operationAmount": {"currency": {"code": "USD"}, "amount": "1.0"}}
        result = currency_conversion(transaction)
        self.assertEqual(result, 75.0)


if __name__ == "__main__":
    unittest.main()
