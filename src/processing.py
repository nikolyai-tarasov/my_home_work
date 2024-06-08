def sort_to_state(my_dict: list, state_='EXECUTED') -> list:
    """Функция сортирует списки словарей по второму заданному аргументу"""
    return_list = []
    for i in my_dict:
        if i['state'] == state_:
            return_list.append(i)
    return return_list


print(sort_to_state([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                     {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                     {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                     {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}], 'CANCELED'))
