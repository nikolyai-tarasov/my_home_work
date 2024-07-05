import json


def read_file(filename: str = None) -> list:
    """Функция считывающая информацию JSON формата с заданного файла"""
    with open(filename, encoding="utf-8") as file:
        reading = json.load(file)
        if type(reading) is not list or len(reading) == 0 or filename is None:
            return []
    return reading


transaction = read_file("../data/operations.json")

