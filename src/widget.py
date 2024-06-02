from src.masks import masking_cards, check_mask


def info_cart(info: str) -> str:
    if 'Счет' in info:
        return f"{info[0:5]} {check_mask(info[-20:])}"
    elif 'Счет' not in info:
        cart_name = ''
        cart_num = ''
        for i in info:
            if i.isalpha():
                cart_name += i
            elif i.isdigit():
                cart_num += i
    return f"{cart_name} {masking_cards(cart_num)}"
