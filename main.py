from src.external_api import read_file
from src.reading_excel_file import read_excel
from src.reading_csv_file import read_csv
from src.processing import filter_by_state


def main():
    access = True
    print('''Привет! Добро пожаловать в программу работы 
с банковскими транзакциями. 
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла''')
    user_input = input()
    if '1' in user_input:
        print("Для обработки выбран JSON-файл.")
        transaction_file = read_file("../data/data_json/operation.json")
    elif "2" in user_input:
        print("Для обработки выбран CSV-файл.")
        transaction_file = read_csv("data/data_csv-/transactions.csv")
    elif "3" in user_input:
        print("Для обработки выбран XLSX-файл.")
        transaction_file = read_excel("data/data_xlsx/transactions_excel.xlsx")

    while access:
        user_status = input('''Введите статус, по которому необходимо выполнить фильтрацию. 
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING
''')
        if user_status.upper() == "EXECUTED" or user_status.upper() == "CANCELED" or user_status.upper() == "PENDING":
            access = False
            sort_by_status = filter_by_state(transaction_file, user_status.upper())
            print(sort_by_status)
        else:
            print(f"Статус операции {user_status} недоступен.")

    print("Отсортировать операции по дате? Да/Нет")
    date_sorted = input()
    print("Отсортировать по возрастанию или по убыванию?")
    sorting_direction = input()
    print("Выводить только рублевые транзакции? Да/Нет")
    print('''Отфильтровать список транзакций по определенному слову 
в описании? Да/Нет''')
    print("Распечатываю итоговый список транзакций...")
    print("Всего банковских операций в выборке:")


if __name__ == "__main__":
    print(main())
