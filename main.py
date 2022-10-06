import csv
import datetime
import json
import time

from operation import Operation
from checking import Fraud
import xlsxwriter

PATTERNS = {
    "MANY_CLICKS": 1,  # проверка на множество кликов с одного ID
    "EQUAL_DELAY": 2,  # проверка на равные промежутки времени между операциями
    "NIGHT_TIME": 3  # поверка на подозрительную активность в ночное время
}
JSON_FILENAME = "transactions.json"
FILENAME = "data.csv"


def write_to_csv():
    with open(FILENAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(('date', 'card', 'account', 'client',
                         'age', 'result',
                         'terminal_type', 'city', 'phone', 'amount'))
        for operation in get_operations():
            writer.writerow((operation.date, operation.card, operation.account, operation.client,
                             float(datetime.datetime.now().year - operation.date_of_birth.year),
                             operation.oper_result, operation.terminal_type, operation.city,
                             operation.phone, operation.amount))


# считывание операций из исходного файла
def get_operations() -> list[Operation]:
    with open(JSON_FILENAME, "r") as f:
        transactions_json = f.read()
    transactions = json.loads(transactions_json)

    operations = []
    for op_id, op_data in transactions['transactions'].items():
        obj = Operation(op_id, op_data)
        operations.append(obj)
    return operations


# функция добавления мошеннической операции в таблицу
def append_xlsx(pattern_num: str, operation: str) -> None:
    pass


def main():
    checker = Fraud(get_operations())
    night_ids = [x.id for x in checker.day_time()]
    operations = get_operations()
    print(night_ids)
    types = set()
    t = set()
    for el in operations:
        types.add(el.oper_result)
        t.add(el.oper_type)
    print(t)
    print(types)
    write_to_csv()

    # проверка на одинаковые временные промежутки
    op_with_delay_equal = checker.equal_delay()
    if len(op_with_delay_equal):
        for operation in op_with_delay_equal:
            append_xlsx(str(PATTERNS['EQUAL_DELAY']), operation.id)

    patterns = {"3": list(night_ids)}
    row, col = 0, 0
    workbook = xlsxwriter.Workbook('Result.xlsx')
    worksheet = workbook.add_worksheet()

    for key, value in patterns.items():
        worksheet.write(row, col, key)
        worksheet.write(row, col + 1, ', '.join(str(x) for x in sorted(value)))
        row += 1
    workbook.close()


if __name__ == '__main__':
    main()
