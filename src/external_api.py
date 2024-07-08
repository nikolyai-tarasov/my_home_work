import os

import requests
from dotenv import load_dotenv

from src.utils import read_file

load_dotenv(".env")

API_KEY = os.getenv("API_KEY")


def currency_conversion(transaction: list) -> float:
    """Функция конвертации валюты"""
    count_sum_amount = 0
    url_usd = "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount="
    url_eur = "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=EUR&amount="
    if transaction[0]["operationAmount"]["currency"]["code"] == "USD":
        url_1 = f"{url_usd}{transaction[0]["operationAmount"]['amount']}"
        payload = {}
        headers = {"apikey": API_KEY}
        response = requests.request("GET", url_1, headers=headers, data=payload)
        status_code = response.status_code
        result = response.json()
        return result['result']
    elif transaction[0]["operationAmount"]["currency"]["code"] == "EUR":
        url_1 = f"{url_eur}{transaction[0]["operationAmount"]["amount"]}"
        payload = {}
        headers = {"apikey": API_KEY}
        response = requests.request("GET", url_1, headers=headers, data=payload)
        status_code = response.status_code
        result = response.json()
        return result['result']
    else:
        count_sum_amount += float(transaction[0]["operationAmount"]["amount"])

    return count_sum_amount


if __name__ == "__main__":
    res_func = read_file("../data/tests_operations.json")
    print(currency_conversion(res_func))
