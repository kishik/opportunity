import json
from operation import Operation
import checking


def recieving():
    # Use a breakpoint in the code line below to debug your script.
    with open("transactions.json", "r") as my_file:
        transactions_json = my_file.read()  # Press Ctrl+F8 to toggle the breakpoint.
    transactions = json.loads(transactions_json)

    result = []
    for el, elv in transactions['transactions'].items():
        obj = Operation(id=el, kwargs=elv)
        result.append(obj)

        print(obj.id)
    return result


if __name__ == '__main__':
    operations = recieving()
    print(len(operations))
