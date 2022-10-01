from datetime import datetime


class Operation:

    def __init__(self, id, **kwargs):
        self.id = id
        self.card = kwargs['kwargs']['card']
        self.account = kwargs['kwargs']['account']
        self.client = kwargs['kwargs']['client']
        self.last_name = kwargs['kwargs']['last_name']
        self.first_name = kwargs['kwargs']['first_name']
        self.patronymic = kwargs['kwargs']['patronymic']
        self.passport = kwargs['kwargs']['passport']
        self.phone = kwargs['kwargs']['phone']
        self.oper_type = kwargs['kwargs']['oper_type']
        self.amount = kwargs['kwargs']['amount']
        self.oper_result = kwargs['kwargs']['oper_result']
        self.terminal = kwargs['kwargs']['terminal']
        self.terminal_type = kwargs['kwargs']['terminal_type']
        self.city = kwargs['kwargs']['city']
        self.address = kwargs['kwargs']['address']
        self.date = datetime.strptime(kwargs['kwargs']['date'], "%Y-%m-%dT%H:%M:%S")
        try:
            self.account_valid_to = datetime.strptime(kwargs['kwargs']['account_valid_to'], "%Y-%m-%dT%H:%M:%S")
            self.date_of_birth = datetime.strptime(kwargs['kwargs']['date_of_birth'], "%Y-%m-%dT%H:%M:%S")
            self.passport_valid_to = datetime.strptime(kwargs['kwargs']['passport_valid_to'], "%Y-%m-%dT%H:%M:%S")
        except ValueError:
            self.account_valid_to = datetime.strptime(kwargs['kwargs']['account_valid_to'], "%Y-%m-%d")
            self.date_of_birth = datetime.strptime(kwargs['kwargs']['date_of_birth'], "%Y-%m-%d")
            self.passport_valid_to = datetime.strptime(kwargs['kwargs']['passport_valid_to'], "%Y-%m-%d")
