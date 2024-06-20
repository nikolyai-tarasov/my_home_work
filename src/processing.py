from typing import Union


def filter_by_state(my_dict: list, state_: str = "EXECUTED") -> Union[list, str]:
    """Функция сортирует списки словарей по второму заданному аргументу"""
    return_list = []
    for i in my_dict:
        if i["state"] == state_:
            return_list.append(i)
        elif state_ != "EXECUTED" and state_ != "CANCELED":
            return "Введите корректный 2 аргумент"

    return return_list


def sort_by_date(my_dict: list, direction: bool = True) -> Union[list, str]:
    """Функция для сортировки словарей по дате"""
    if isinstance(my_dict, list) and direction != bool:
        sort_by_date_ = sorted(my_dict, key=lambda my_dict: my_dict.get("date"), reverse=direction)
        return sort_by_date_
    return "Вы ввели не соответствующие данные"
