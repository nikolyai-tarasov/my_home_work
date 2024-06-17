def filter_by_currency(transaction: list, currency: str) -> dict:
    """Функция принимающая список словарей и возвращает банковскую операцию по заданной валюте"""
    if transaction == list(transaction) and currency == str(currency):
        for i in transaction:
            if i["operationAmount"]["currency"]["code"] == currency:
                yield i['id']
    else:
        yield "Введены не верные данные"


def transaction_descriptions(transaction: list) -> str:
    """Функция принимающая список словарей и возвращает описание операции"""
    for i in transaction:
        yield i["description"]
    else:
        yield "Введены не верные данные"


def card_number_generator(start, stop):
    """Функция генерации номера банковских карт"""
    if start == int(start) and stop == int(stop):
        number_card = list(range(start, stop))
        zero = "0000 0000 0000 0000"
        for i in number_card:
            length_num = len(str(i))
            yield f"{zero[0: 19 - length_num]}{str(i)}"
    else:
        yield "Введены не верные данные"



