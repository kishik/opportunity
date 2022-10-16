from backend.db.sqllib import SQLlib
from backend.transaction import Operation
from backend.fraud import Fraud


def get_transaction_from_json(data: dict) -> list[Operation]:
    transactions = []
    for t_id, t_data in data['transactions'].items():
        obj = Operation(t_id, t_data)
        transactions.append(obj)
    return transactions


def get_fraud_transactions(data: dict) -> dict:
    result = {
        "fraud_transactions": []
    }
    transactions = get_transaction_from_json(data)
    f = Fraud(transactions)
    fraud_transactions = f.many_clicks()
    fraud_transactions.extend(f.equal_delay())
    fraud_transactions.extend(f.day_time())
    fraud_transactions = set(fraud_transactions)
    for transaction in fraud_transactions:
        result['fraud_transactions'].append(transaction.to_dict())
    return result


class Helper:

    def __init__(self) -> None:
        self.sql = SQLlib()

    def add_transactions_to_db(self, data: dict) -> None:
        transactions = data['transactions']
        for transactions_id, t_data in transactions.items():
            self.sql.add_transaction(transactions_id, t_data)

    def get_all_transactions(self) -> dict:
        transactions = self.sql.get_transactions()
        result = {
            "transactions": []
        }
        for t in transactions:
            result['transactions'].append({
                t[0]: {
                    "date": t[1],
                    "card": t[2],
                    "account": t[3],
                    "account_valid_to": t[4],
                    "client": t[5],
                    "last_name": t[6],
                    "first_name": t[7],
                    "patronymic": t[8],
                    "date_of_birth": t[9],
                    "passport": t[10],
                    "passport_valid_to": t[11],
                    "phone": t[12],
                    "oper_type": t[13],
                    "amount": t[14],
                    "oper_result": t[15],
                    "terminal": t[16],
                    "terminal_type": t[17],
                    "city": t[18],
                    "address": t[19]
                }
            })
        return result
