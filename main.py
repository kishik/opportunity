import json
from operation import Operation
from checking import Fraud
import xlsxwriter

PATTERNS = {
    "MANY_CLICKS": 1,  # проверка на множество кликов с одного ID
    "EQUAL_DELAY": 2,  # проверка на равные промежутки времени между операциями
    "NIGHT_TIME": 3  # поверка на подозрительную активность в ночное время
}
JSON_FILENAME = "transactions.json"


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

    print(result)

    '''
    patterns = {"1": [1, 2, 4], "5": [21312, 324236, 231]}
    row, col = 0, 0
    workbook = xlsxwriter.Workbook('Result.xlsx')
    worksheet = workbook.add_worksheet()

    for key, value in patterns.items():
        worksheet.write(row, col, key)
        worksheet.write(row, col + 1, ', '.join(str(x) for x in sorted(value)))
        row += 1
    workbook.close()
    '''


if __name__ == '__main__':
    main()
