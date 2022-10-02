import json
from operation import Operation
from checking import *
import xlsxwriter
import copy


def receiving() -> list[Operation]:
    # Use a breakpoint in the code line below to debug your script.
    with open("transactions.json", "r") as my_file:
        transactions_json = my_file.read()  # Press Ctrl+F8 to toggle the breakpoint.
    transactions = json.loads(transactions_json)

    result = []
    for el, elv in transactions['transactions'].items():
        obj = Operation(el, elv)
        result.append(obj)

        print(obj.id)
    return result


if __name__ == '__main__':
    operations = receiving()
    print(len(operations))

    for operation in day_time(operations):
        print(operation.id)

    patterns = {"1": [1, 2, 4], "5": [21312, 324236, 231]}
    row, col = 0, 0
    workbook = xlsxwriter.Workbook('Result.xlsx')
    worksheet = workbook.add_worksheet()

    for key, value in patterns.items():
        worksheet.write(row, col, key)
        worksheet.write(row, col + 1, ', '.join(str(x) for x in sorted(value)))
        row += 1
    workbook.close()

