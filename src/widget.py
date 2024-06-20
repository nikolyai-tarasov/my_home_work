from src.masks import check_mask, masking_cards


def info_cart(info: str) -> str:
    """Улучшенная функция маскировки"""

    if "Счет" in info:
        return f"{info[0:5]} {check_mask(info[-20:])}"
    elif "Счет" not in info:
        cart_name = ""
        cart_num = ""
        for i in info:
            if i.isalpha():
                cart_name += i
            elif i.isdigit():
                cart_num += i
    return f"{cart_name} {masking_cards(cart_num)}"


def transformation_date(date: str) -> str:
    """Функция преобразовывающая дату"""
    if len(date) == 26:
        return f"{date[8:10]}.{date[5:7]}.{date[0:4]}"
    else:
        return "Введена не корректная дата"


print(transformation_date("2023-12-13T02:26:18.671407"))
