from typing import List, Any

df = [
    {'id': '3400097', 'state': 'EXECUTED', 'date': '2021-09-26T11:05:08Z', 'amount': '15109',
     'currency_name': 'Yuan Renminbi', 'currency_code': 'CNY', 'from': '', 'to': 'Счет 69849544853538949269',
     'description': 'Открытие вклада'}, {'id': '4399167', 'state': 'EXECUTED', 'date': '2023-07-08T22:43:16Z',
                                         'amount': '23949', 'currency_name': 'Peso', 'currency_code': 'PHP',
                                         'from': 'Discover 8086808716905997', 'to': 'Visa 0250616482559995',
                                         'description': 'Перевод с карты на карту'},
    {'id': '5446796', 'state': 'EXECUTED',
     'date': '2020-10-06T23:30:05Z',
     'amount': '26873',
     'currency_name': 'Euro',
     'currency_code': 'EUR', 'from': '',
     'to': 'Счет 18984367308636722946',
     'description': 'Открытие вклада'}, {
        'id': '2177828', 'state': 'EXECUTED', 'date': '2022-04-14T15:14:21Z', 'amount': '24853',
        'currency_name': 'Yuan Renminbi', 'currency_code': 'CNY', 'from': 'Счет 38577962752140632721',
        'to': 'Счет 47657753885349826314', 'description': 'Перевод со счета на счет'}, {'id': '4137938',
                                                                                        'state': 'EXECUTED',
                                                                                        'date': '2023-01-04T13:13:34Z',
                                                                                        'amount': '15560',
                                                                                        'currency_name': 'Real',
                                                                                        'currency_code': 'BRL',
                                                                                        'from': '',
                                                                                        'to': 'Счет 38164279390569873521',
                                                                                        'description': 'Открытие вклада'},
    {
        'id': '4699552', 'state': 'EXECUTED', 'date': '2022-03-23T08:29:37Z', 'amount': '23423', 'currency_name': 'RUB',
        'currency_code': 'PHP', 'from': 'Discover 7269000803370165', 'to': 'American Express 1963030970727681',
        'description': 'Перевод с карты на карту'}]


def filter_trans(list_dict: list, currency: str) -> list[Any] | str:
    """Функция фильтрующая списки словарей по валюте"""
    list_currency = []
    for i in list_dict:
        if "operationAmount" in i:
            if i["operationAmount"]["currency"]["code"] == currency:
                list_currency.append(i)
                return list_currency

        elif i['currency_name'] == currency:
            list_currency.append(i)
            return list_currency
        continue
    return "Ничего нe найдено"



