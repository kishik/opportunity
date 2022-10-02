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
        self.passport = data['passport']
        self.phone = data['phone']
        self.oper_type = data['oper_type']
        self.amount = data['amount']
        self.oper_result = data['oper_result']
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
