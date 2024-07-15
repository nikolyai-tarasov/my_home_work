import pandas as pd


def read_excel(path_file: str) -> list[dict]:
    """
    Функция читает .xlsx файл и возвращает список словарей
    """
    df = pd.read_excel(path_file)
    result = df.apply(
        lambda row: {
            "id": row["id"],
            "state": row["state"],
            "date": row["date"],
            "operationAmount": {
                "amount": row["amount"],
                "currency": {"name": row["currency_name"], "code": row["currency_code"]},
            },
            "description": row["description"],
            "from": row["from"],
            "to": row["to"],
        },
        axis=1,
    ).tolist()
    return result


# "../data/data_csv-/transactions.csv"
if __name__ == "__main__":
    print(read_excel("../data/data_xlsx/transactions_excel.xlsx"))
