def filter_by_state(my_dict: list, state_='EXECUTED') -> list:
    """Функция сортирует списки словарей по второму заданному аргументу"""
    return_list = []
    for i in my_dict:
        if i['state'] == state_:
            return_list.append(i)
    return return_list


def sort_by_date(my_dict: list, direction: bool = True) -> list:
    """Функция для сортировки словарей по дате"""
    sort_by_date_ = sorted(my_dict, key=lambda my_dict: my_dict.get("date"), reverse=direction)
    return sort_by_date_
