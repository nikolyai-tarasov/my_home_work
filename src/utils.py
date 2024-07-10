import json
import logging

logger = logging.getLogger("utils")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("../logs/utils.log", "w")
file_formater = logging.Formatter("%(asctime)s %(filename)s %(levelname)s %(message)s")
file_handler.setFormatter(file_formater)
logger.addHandler(file_handler)


def read_file(filename: str = None) -> list:
    """Функция считывающая информацию JSON формата с заданного файла"""
    if filename is not None:
        try:
            logger.info('Начало работы с "json" файлом')
            with open(filename, encoding="utf-8") as file:
                reading = json.load(file)
                logger.info("Проверка созданного файла")
                if type(reading) is not list or len(reading) == 0 or filename is None:
                    return []
            return reading
        except (FileNotFoundError, json.JSONDecodeError):
            logger.error(f"Произошла ошибка: {FileNotFoundError}")
            return []
    else:
        logger.info(f"Не подходящий формат: {type(filename)}")
        return []


if __name__ == "__main__":
    read_file()
