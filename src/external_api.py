import os

import requests
from dotenv import load_dotenv

from src.utils import read_file

load_dotenv(".env")

API_KEY = os.getenv("API_KEY")


def currency_conversion(transaction: list) -> float:
    """Функция конвертации валюты"""
    count_sum_amount = 0
    url = "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=EUR&amount="
    if transaction[0]["operationAmount"]["currency"]["code"] == "USD":
        url_1 = f"{url}{transaction[0]["operationAmount"]['amount']}"
        payload = {}
        headers = {"apikey": API_KEY}
        response = requests.request("GET", url_1, headers=headers, data=payload)
        status_code = response.status_code
        result = response.json()
        count_sum_amount += result["result"]
        return count_sum_amount
    elif transaction[0]["operationAmount"]["currency"]["code"] == "EUR":
        url_1 = f"{url}{transaction[0]["operationAmount"]["amount"]}"
        payload = {}
        headers = {"apikey": API_KEY}
        response = requests.request("GET", url_1, headers=headers, data=payload)
        status_code = response.status_code
        result = response.json()
        count_sum_amount += result["result"]
        return count_sum_amount
    else:
        count_sum_amount += float(transaction[0]["operationAmount"]["amount"])

    return count_sum_amount


if __name__ == "__main__":
    res_func = read_file("../data/operations.json")
    print(currency_conversion(res_func))
