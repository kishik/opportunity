"""
Тут хранится класс описыващий операцию
"""
from datetime import datetime


class Operation:

    def __init__(self, operation_id, data):
        self.id = operation_id
        self.card = data['card']
        self.account = data['account']
        self.client = data['client']
        self.last_name = data['last_name']
        self.first_name = data['first_name']
        self.patronymic = data['patronymic']
        self.passport = str(data['passport'])
        self.phone = data['phone']
        if int(data['oper_type']) < 0:
            raise ValueError
        self.oper_type = data['oper_type']
        self.amount = data['amount']
        if data['oper_result'] == "Отказ":
            self.oper_result = 0
        else:
            self.oper_result = 1
        self.terminal = data['terminal']
        self.terminal_type = data['terminal_type']
        self.city = data['city']
        self.address = data['address']
        self.date = datetime.strptime(data['date'], "%Y-%m-%dT%H:%M:%S")
        try:
            self.account_valid_to = datetime.strptime(data['account_valid_to'], "%Y-%m-%dT%H:%M:%S")
            self.date_of_birth = datetime.strptime(data['date_of_birth'], "%Y-%m-%dT%H:%M:%S")
            self.passport_valid_to = datetime.strptime(data['passport_valid_to'], "%Y-%m-%dT%H:%M:%S")
        except ValueError:
            self.account_valid_to = datetime.strptime(data['account_valid_to'], "%Y-%m-%d")
            self.date_of_birth = datetime.strptime(data['date_of_birth'], "%Y-%m-%d")
            self.passport_valid_to = datetime.strptime(data['passport_valid_to'], "%Y-%m-%d")

    def to_dict(self) -> dict:
        return {
                "date": str(self.date),
                "card": self.card,
                "account": self.account,
                "client": self.client,
                "last_name": self.last_name,
                "first_name": self.first_name,
                "patronymic": self.patronymic,
                "passport": self.passport,
                "phone": self.phone,
                "oper_type": self.oper_type,
                "amount": self.amount,
                "terminal": self.terminal,
                "terminal_type": self.terminal_type,
                "city": self.city,
                "address": self.address,
                "oper_result": "Успешно" if self.oper_result else "Отказ",
                "account_valid_to": str(self.account_valid_to),
                "date_of_birth": str(self.date_of_birth),
                "passport_valid_to": str(self.passport_valid_to)
            }