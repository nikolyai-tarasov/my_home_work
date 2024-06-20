import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency():
    assert (
        next(
            filter_by_currency(
                [
                    {
                        "id": 939719570,
                        "state": "EXECUTED",
                        "date": "2018-06-30T02:08:58.425572",
                        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
                        "description": "Перевод организации",
                        "from": "Счет 75106830613657916952",
                        "to": "Счет 11776614605963066702",
                    }
                ],
                "USD",
            )
        )
        == 939719570
    )


def test_transaction_descriptions(condition_else):
    assert (
        next(
            transaction_descriptions(
                [
                    {
                        "id": 939719570,
                        "state": "EXECUTED",
                        "date": "2018-06-30T02:08:58.425572",
                        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
                        "description": "Перевод организации",
                        "from": "Счет 75106830613657916952",
                        "to": "Счет 11776614605963066702",
                    }
                ]
            )
        )
        == "Перевод организации"
    )
    assert next(transaction_descriptions([])) == condition_else


def test_card_number_generator(condition_else):
    assert next(card_number_generator(1, 2)) == "0000 0000 0000 0001"
    assert next(card_number_generator(1, "1")) == condition_else


@pytest.mark.parametrize(
    "value, expected",
    [
        (1, "0000 0000 0000 0001"),
        ("12", "Введены не верные данные"),
    ],
)
def test_card_generator(value, expected):
    assert next(card_number_generator(value, 12)) == expected
