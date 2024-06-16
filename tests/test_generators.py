import pytest
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


def test_filter_by_currency():
    assert next(filter_by_currency([{
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }], 'USD')) == "939719570"



def test_transaction_descriptions():
    assert next(transaction_descriptions([{
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }])) == "Перевод организации"
    assert next(transaction_descriptions([])) == "Введены не верные данные"


def test_card_number_generator():
    assert next(card_number_generator(1, 2)) == "0000 0000 0000 0001"
