from collections import Counter


def count_operation(list_dict: list, list_category: list) -> dict:
    """Функция подсчета количества категорий в списке словарей по списку категории"""
    name_category = []
    counter_dict = {}
    for i in list_dict:
        name_category.append(i["description"])
    counter_category = Counter(name_category)
    cortege_category = counter_category.most_common()
    for i in list_category:
        for c in cortege_category:
            if i == c[0]:
                counter_dict[i] = c[1]
    return counter_dict
