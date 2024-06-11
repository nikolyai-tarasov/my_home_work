def masking_cards(num_cards: str) -> str:
    """Функция маскирует номер карты пользователя"""

    if num_cards.isdigit() and len(num_cards) == 16:
        return f"{num_cards[0:4]} {num_cards[4:6]}{"*" * 2} {"*" * 4} {num_cards[12:]}"
    else:
        return "Не верно введен номер карты"


def check_mask(num_check: str) -> str:
    """Функция маскирует номер счета"""
    if num_check.isdigit() and len(num_check) == 20:
        return f"{"*" * 2}{num_check[-4:]}"
    else:
        return "Не верно введен номер счета"
