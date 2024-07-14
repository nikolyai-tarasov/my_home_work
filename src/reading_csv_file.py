import csv


def read_csv(path_file):
    """
    Функция читает CSV файл и возвращает список словарей
    """
    with open(path_file, "r", encoding="utf-8") as file:
        reader = csv.reader(file, delimiter=";")
        header = next(reader)
        result = []
        for row in reader:
            row_dict = dict()
            for ind, itm in enumerate(header):
                row_dict[itm] = row[ind]
            result.append(row_dict)
        return result


# "../data/data_csv-/transactions.csv"
if __name__ == "__main__":
    print(read_csv("../data/data_csv-/transactions.csv"))
