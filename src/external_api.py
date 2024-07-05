import json
import os
import requests
from src.utils import read_file
from dotenv import load_dotenv

load_dotenv(".env")

API_KEY = os.getenv("API_KEY")


def currency_conversion(transaction: list) -> float:
    """Функция конвертации валюты"""
    count_sum_amount = 0
    if transaction["operationAmount"]["currency"]["code"] == "USD":
        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount={transaction['operationAmount']['amount']}"
        payload = {}
        headers = {"apikey": API_KEY}
        response = requests.request("GET", url, headers=headers, data=payload)
        status_code = response.status_code
        result = response.json()
        count_sum_amount += result["result"]
    elif transaction["operationAmount"]["currency"]["code"] == "EUR":
        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=EUR&amount={transaction['operationAmount']['amount']}"
        payload = {}
        headers = {"apikey": API_KEY}
        response = requests.request("GET", url, headers=headers, data=payload)
        status_code = response.status_code
        result = response.json()
        count_sum_amount += result["result"]
    else:
        count_sum_amount += float(transaction["operationAmount"]["amount"])

    return count_sum_amount


res_func = read_file("../data/operations.json")
print(currency_conversion(res_func))
