import requests

from backend.db.sqllib import SQLlib
from backend.fraud import Fraud
from backend.transaction import Operation

API_KEY = ''


def get_transaction_from_json(data: dict) -> list[Operation]:
    transactions = []
    for t_id, t_data in data['transactions'].items():
        obj = Operation(t_id, t_data)
        transactions.append(obj)
    return transactions


def get_fraud_transactions(data: dict) -> dict:
    result = {
        "fraud_transactions": {
            "pattern_1": {
                "transactions": [],
                "count": 0
                },
            "pattern_2": {
                "transactions": [],
                "count": 0
            },
            "pattern_3": {
                "transactions": [],
                "count": 0
            }
        }
    }
    transactions = get_transaction_from_json(data)
    f = Fraud(transactions)
    for t in f.many_clicks():
        result['fraud_transactions']['pattern_1']['transactions'].append(t.id)
    result['fraud_transactions']['pattern_1']['count'] = len(result['fraud_transactions']['pattern_1']['transactions'])
    for t in f.equal_delay():
        result['fraud_transactions']['pattern_2']['transactions'].append(t.id)
    result['fraud_transactions']['pattern_2']['count'] = len(result['fraud_transactions']['pattern_2']['transactions'])
    for t in f.day_time():
        result['fraud_transactions']['pattern_3']['transactions'].append(t.id)
    result['fraud_transactions']['pattern_3']['count'] = len(result['fraud_transactions']['pattern_3']['transactions'])
    return result


class Helper:

    def __init__(self) -> None:
        self.sql = SQLlib()
        self.city_api_url = \
            'http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit=1&appid={api_key}'

    def get_city_lat_lon(self, name: str) -> list[str]:
        req = requests.get(self.city_api_url.format(name, API_KEY)).json()
        return [req[0]['lat'], req[0]['lon']]

    def add_transactions_to_db(self, data: dict) -> None:
        transactions = data['transactions']
        for transactions_id, t_data in transactions.items():
            self.sql.add_transaction(transactions_id, t_data)
            if not self.sql.check_city(t_data['city']):
                pass

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
