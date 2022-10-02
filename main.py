import json
from operation import Operation
import checking
import xlsxwriter


JSON_FILENAME = "transactions.json"


# считывание операций из исходного файла
def get_operations():

    with open(JSON_FILENAME, "r") as f:
        transactions_json = f.read()
    transactions = json.loads(transactions_json)

    operations = []
    for op_id, op_data in transactions['transactions'].items():
        obj = Operation(op_id, op_data)
        operations.append(obj)
    return operations


def main():
    operations = get_operations()
    patterns = {"1": [1, 2, 4], "5": [21312, 324236, 231]}
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

