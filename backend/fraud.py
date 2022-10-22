"""
Тут хранится класс для проверки операций
"""
from datetime import datetime, timedelta

from backend.transaction import Operation


class Fraud:
    def __init__(self, operations: list[Operation]) -> None:
        self.operations = operations

    #  получение операций от конкретного клиента
    def operations_by_client(self, client: str) -> list[Operation]:
        return [operation for operation in self.operations if operation.client == client]

    def accounts(self) -> list[str]:
        return list(set([operation.account for operation in self.operations]))

    #  получение операций от конкретного аккаунта
    def operations_by_account(self, account: str) -> list[Operation]:
        return [operation for operation in self.operations if operation.account == account]

    #  получение операции с конкретного устройства (terminal)
    def operations_by_terminal(self, terminal: str) -> list[Operation]:
        return [operation for operation in self.operations if operation.terminal == terminal]

    #  проверка на множество кликов с одного ID
    def many_clicks(self, minutes=5) -> list[Operation]:
        acceracy = timedelta(minutes=minutes)  # промежуток времени в 5 минут
        checked_terminals = {}
        fraud_operations = []
        for i in range(len(self.operations)):
            if not checked_terminals.get(self.operations[i].terminal):
                terminal_operations = self.operations_by_terminal(self.operations[i].terminal)
                for j in range(1, len(terminal_operations)):
                    if terminal_operations[j].date - terminal_operations[j].date <= acceracy:
                        fraud_operations.append(terminal_operations[j])
                checked_terminals[self.operations[i].terminal] = 1
        return fraud_operations

    #  проверка на одинаковые временные промежутки между операциями
    def equal_delay(self, seconds=1) -> list[Operation]:
        acceracy = timedelta(seconds=seconds)  # погрешность в 1 секунду
        checked_clients = {}
        temp = None
        fraud_operations = []
        for i in range(len(self.operations)):
            if not checked_clients.get(self.operations[i].client):
                client_operation = self.operations_by_client(self.operations[i].client)
                for j in range(1, len(client_operation)):
                    if not temp:
                        temp = client_operation[j].date - client_operation[j - 1].date
                    else:
                        div = client_operation[j].date - client_operation[j - 1].date
                        if div == temp or div == temp + acceracy or div == temp - acceracy:
                            fraud_operations.append(client_operation[j])
                        temp = div
                checked_clients[self.operations[i].client] = 1
        return fraud_operations

    #  проверка на подозрительную активность в ночное время
    def outdated_account(self) -> list[Operation]:
        return list(filter(lambda x: x.account_valid_to < datetime.now(), self.operations))

    def bad_time(self, time) -> list[Operation]:
        if time[0] > time[1]:
            return list(filter(lambda x: x.date.hour >= time[0] or x.date.hour <= time[1], self.operations))
        return list(filter(lambda x: time[0] <= x.date.hour <= time[1], self.operations))

    def bad_age(self, age):
        return list(
            filter(lambda x: min(age) <= datetime.now().year - x.date_of_birth.year <= max(age), self.operations))

    def outdated_passport(self) -> list[Operation]:
        return list(filter(lambda x: x.passport_valid_to < datetime.now(), self.operations))

    def diff_cities(self, minutes) -> list[Operation]:
        result = []
        for account in self.accounts():
            account_operations = self.operations_by_account(account)
            if len(account_operations) < 2:
                continue
            for i in range(1, len(account_operations)):
                if account_operations[i].city != account_operations[i - 1].city and \
                        (account_operations[i].date - account_operations[i - 1].date).total_seconds() > minutes * 60:
                    if i >= 3:
                        if account_operations[i - 2].city == account_operations[i - 1].city:
                            result.append(account_operations[i])
                        elif account_operations[i - 2].city == account_operations[i].city:
                            result.append(account_operations[i - 1])
                        else:
                            result.extend((account_operations[i - 1], account_operations[i]))
                        continue
                    result.extend((account_operations[i - 1], account_operations[i]))
        return result
