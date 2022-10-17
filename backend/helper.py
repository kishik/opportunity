import requests

from backend.db.sqllib import SQLlib
from backend.fraud import Fraud
from backend.transaction import Operation

API_KEY = '267c99ba130b445b455b4aa7d9b5e617'

BAD_HOURS = (14, 16)
AGE = (58, 63)
MANY_CLICKS_DELAY = 5
EQUAL_DELAY = 1
NIGHT_HOURS = (0, 5)


def get_transaction_from_json(data: dict) -> list[Operation]:
    transactions = []
    for t_id, t_data in data['transactions'].items():
        obj = Operation(t_id, t_data)
        transactions.append(obj)
    return transactions


def set_many_clicks_data(delay: int) -> None:
    global MANY_CLICKS_DELAY
    MANY_CLICKS_DELAY = delay
    print(delay)


def set_bad_time_data(time_f: int, time_t: int) -> None:
    global BAD_HOURS
    BAD_HOURS = (time_f, time_t)
    print(time_f, time_t)


def set_night_time_data(time_f: int, time_t: int) -> None:
    global NIGHT_HOURS
    NIGHT_HOURS = (time_f, time_t)
    print(time_f, time_t)


def set_bad_age_data(age_f: int, age_t: int) -> None:
    global AGE
    AGE = (age_f, age_t)
    print(age_f, age_t)


def set_equal_delay_data(delay: int) -> None:
    global EQUAL_DELAY
    EQUAL_DELAY = delay
    print(delay)


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
            },
            "pattern_4": {
                "transactions": [],
                "count": 0
            },
            "pattern_5": {
                "transactions": [],
                "count": 0
            },
            "pattern_6": {
                "transactions": [],
                "count": 0
            }
        }
    }
    transactions = get_transaction_from_json(data)
    f = Fraud(transactions)
    # for i in range(len(bad_time)):
    #     result['fraud_transactions']['pattern_3']['transactions'] = [t.id for t in f.night_time()]
    #     result['fraud_transactions']['pattern_3']['count'] = len(
    #         result['fraud_transactions']['pattern_3']['transactions'])
    result['fraud_transactions']['pattern_1']['transactions'] = [t.id for t in f.many_clicks(MANY_CLICKS_DELAY)]
    result['fraud_transactions']['pattern_1']['count'] = len(result['fraud_transactions']['pattern_1']['transactions'])
    result['fraud_transactions']['pattern_2']['transactions'] = [t.id for t in f.equal_delay(EQUAL_DELAY)]
    result['fraud_transactions']['pattern_2']['count'] = len(result['fraud_transactions']['pattern_2']['transactions'])
    result['fraud_transactions']['pattern_3']['transactions'] = [t.id for t in f.bad_time(NIGHT_HOURS)]
    result['fraud_transactions']['pattern_3']['count'] = len(result['fraud_transactions']['pattern_3']['transactions'])
    result['fraud_transactions']['pattern_4']['transactions'] = [t.id for t in f.outdated_account()]
    result['fraud_transactions']['pattern_4']['count'] = len(result['fraud_transactions']['pattern_4']['transactions'])
    result['fraud_transactions']['pattern_5']['transactions'] = [t.id for t in f.bad_time(BAD_HOURS)]
    result['fraud_transactions']['pattern_5']['count'] = len(result['fraud_transactions']['pattern_5']['transactions'])
    result['fraud_transactions']['pattern_6']['transactions'] = [t.id for t in f.bad_age(AGE)]
    result['fraud_transactions']['pattern_6']['count'] = len(result['fraud_transactions']['pattern_6']['transactions'])
    return result


class Helper:

    def __init__(self) -> None:
        self.sql = SQLlib()
        self.city_api_url = \
            'http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit=1&appid={api_key}'

    def get_city_lat_lon(self, name: str) -> list[str]:
        req = requests.get(self.city_api_url.format(city_name=name, api_key=API_KEY)).json()
        return [req[0]['lat'], req[0]['lon']]

    def get_transactions_data(self, transaction_ids: str) -> dict:
        result = {
            "transactions": {}
        }
        for t_id in transaction_ids.split(','):
            t = self.sql.get_transaction(t_id)
            result['transactions'][t_id] = {
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
        return result

    def add_transactions_to_db(self, data: dict) -> None:
        transactions = data['transactions']
        for transactions_id, t_data in transactions.items():
            self.sql.add_transaction(transactions_id, t_data)
            if not self.sql.check_city(t_data['city']):
                temp = self.get_city_lat_lon(t_data['city'])
                self.sql.add_city(t_data['city'], temp[0], temp[1])

    def get_all_cities(self) -> dict:
        cities = self.sql.get_cities()
        result = {
            "cities": []
        }
        for c in cities:
            result['cities'].append({
                c[0]: {
                    "lat": c[1],
                    "lon": c[2]
                }
            })
        return result

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
