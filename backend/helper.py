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
