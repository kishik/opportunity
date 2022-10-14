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
    result = {
        "MANY_CLICKS": [],
        "EQUAL_DELAY": [],
        "NIGHT_TIME": []
    }
    # проверка на одинаковые временные промежутки
    op_with_delay_equal = checker.equal_delay()
    if len(op_with_delay_equal):
        for operation in op_with_delay_equal:
            result['EQUAL_DELAY'].append(operation)

    op_with_many_clicks = checker.many_clicks()
    if len(op_with_many_clicks):
        for operation in op_with_many_clicks:
            result['MANY_CLICKS'].append(operation)

    op_with_night_time = checker.day_time()
    if len(op_with_night_time):
        for operation in op_with_night_time:
            result['NIGHT_TIME'].append(operation)

    patterns = {"3": checker.day_time(), "2": checker.equal_delay(), "1": checker.many_clicks()}
    # print(list([int(operation in night_ids) for operation in operations]))
    row, col = 0, 0
    workbook = xlsxwriter.Workbook('Result.xlsx')
    worksheet = workbook.add_worksheet()

    print(patterns)
    for i in range(len(patterns.keys())):
        # print(value)
        worksheet.write(row, col, i + 1)
        worksheet.write(row, col + 1, '[' + ', '.join(sorted(x.id for x in patterns[str(i+1)])) + ']')
        row += 1
    workbook.close()
    '''


if __name__ == '__main__':
    main()
