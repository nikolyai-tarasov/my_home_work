from src.external_api import read_file
from src.reading_excel_file import read_excel
from src.reading_csv_file import read_csv
from src.processing import sort_by_date
from src.processing import filter_by_state
from src.filter_transtion import filter_trans
from src.search_list_dict import search_dict
from src.withdrawal_of_transactions import operation_reverser


def main():
    conter_operation = 0
    global sort_by_status
    access = True

    print('''Привет! Добро пожаловать в программу работы 
с банковскими транзакциями. 
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла''')
    user_input = input()

    if '1' == user_input:
        print("Для обработки выбран JSON-файл.")
        transaction_file = read_file("data/data_json/tests_operations.json")



    elif "2" == user_input:
        print("Для обработки выбран CSV-файл.")
        transaction_file = read_csv("data/data_csv-/transactions.csv")


    elif "3" == user_input:
        print("Для обработки выбран XLSX-файл.")
        transaction_file = read_excel("data/data_xlsx/transactions_excel.xlsx")

    while access:
        user_status = input('''Введите статус, по которому необходимо выполнить фильтрацию. 
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING
''')
        if user_status.upper() == "EXECUTED" or user_status.upper() == "CANCELED" or user_status.upper() == "PENDING":
            access = False
            sort_by_status = filter_by_state(transaction_file, user_status.upper())


        else:
            print(f"Статус операции {user_status} недоступен.")

    print("Отсортировать операции по дате? Да/Нет")
    date_sorted = input()

    if 'Да' in date_sorted:
        print("Отсортировать по возрастанию или по убыванию?")
        sorting_direction = input()

        if "по возрастанию" in sorting_direction:
            sort_date = sort_by_date(sort_by_status)



        elif "по убыванию" in sorting_direction:
            sort_date = sort_by_date(sort_by_status, direction=False)

    print("Выводить только рублевые транзакции? Да/Нет")
    transaction_rubles = input()

    if "Да" in transaction_rubles:

        if "sort_date" in locals():
            sorted_by_trans = filter_trans(sort_date, "RUB")
            if sorted_by_trans == "Ничего нe найдено":
                print('''Не найдено ни одной транзакции, подходящей под ваши
            условия фильтрации''')
                exit()
        else:
            sorted_by_trans = filter_trans(sort_by_status, "RUB")
            if sorted_by_trans == "Ничего нe найдено":
                print('''Не найдено ни одной транзакции, подходящей под ваши
            условия фильтрации''')
                exit()

    print('''Отфильтровать список транзакций по определенному слову 
в описании? Да/Нет''')
    filter_by_word = input()

    if "Да" in filter_by_word:
        filter_words = input('''Введите слово: ''')

        if "sorted_by_trans" in locals():
            print(sorted_by_trans)
            filter_word = search_dict(sorted_by_trans, filter_words)

        elif "sort_date" in locals():
            print(2)
            filter_word = search_dict(sort_date, filter_words)

    print("Распечатываю итоговый список транзакций...")

    if 'filter_word' in locals():
        print(filter_word)
        print(1)
        for i in filter_word:
            conter_operation += 1
            print(operation_reverser(i))
    elif 'sorted_by_trans' in locals():
        print(sorted_by_trans)
        print(2)
        for i in sorted_by_trans:
            conter_operation += 1
            print(operation_reverser(i))
    else:
        print(sort_by_status)
        print(3)
        for i in sort_by_status:
            conter_operation += 1
            print(operation_reverser(i))


if __name__ == "__main__":
    print(main())
