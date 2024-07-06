import logging

logger = logging.getLogger("masks")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("../logs/masks.log", "w")
file_formater = logging.Formatter("%(asctime)s %(filename)s %(levelname)s %(message)s")
file_handler.setFormatter(file_formater)
logger.addHandler(file_handler)


def masking_cards(num_cards: str) -> str:
    """Функция маскирует номер карты пользователя"""
    if num_cards.isdigit() and len(num_cards) == 16:
        logger.info(f"Формирование маски для карты")
        return f"{num_cards[0:4]} {num_cards[4:6]}{"*" * 2} {"*" * 4} {num_cards[12:]}"
    else:
        logger.info(f"Пользователь ввел некорректные номер карты:{num_cards}")
        return "Не верно введен номер карты"


def check_mask(num_check: str) -> str:
    """Функция маскирует номер счета"""
    if num_check.isdigit() and len(num_check) == 20:
        logger.info(f"Формирование маски для cчета")
        return f"{"*" * 2}{num_check[-4:]}"
    else:
        logger.info(f"Пользователь ввел некорректные номер счета: {num_check}")
        return "Не верно введен номер счета"


if __name__ == "__main__":
    masking_cards("1432 4112 3456 3456")
    check_mask("ewrwerewerwer")
