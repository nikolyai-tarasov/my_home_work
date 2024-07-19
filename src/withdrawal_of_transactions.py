from src.widget import transformation_date
from src.widget import info_cart



def operation_reverser(my_dict: dict) -> str:
    """Функция для обработки банковских операций и вывода их пользователю"""
    if 'operationAmount' in my_dict:
        date_operation = transformation_date(my_dict['date'])
        comment = my_dict['description']
        money = f"Сумма: {my_dict['operationAmount']['amount']} {my_dict['operationAmount']['currency']['name']}"
        if 'from' in my_dict:
            masks_to = info_cart(my_dict['to'])
            masks_from = info_cart(my_dict['from'])
            action = f"{masks_from} -> {masks_to}"
        else:
            masks_to = info_cart(my_dict['to'])
            action = f"{masks_to}"
        return f'''{date_operation} {comment}
        {action}
        {money}'''
    elif 'currency_name' in my_dict:
        date_operation = transformation_date(my_dict['date'])
        comment = my_dict['description']
        money = f"Сумма: {my_dict['amount']} {my_dict['currency_name']}"
        if 'from' in my_dict:
            masks_to = info_cart(my_dict['to'])
            masks_from = info_cart(my_dict['from'])
            action = f"{masks_from} -> {masks_to}"
        else:
            masks_to = info_cart(my_dict['to'])
            action = f"{masks_to}"
        return f'''{date_operation} {comment}
{action}
{money}'''




