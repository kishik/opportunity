"""
Тут хранится класс для проверки операций
"""
import operator
from backend.transaction import Operation
from datetime import datetime, timedelta


class Fraud:
    def __init__(self, operations: list[Operation]) -> None:
        self.operations = operations

    #  получение операций от конкретного клиента
    def operations_by_client(self, client: str) -> list[Operation]:
        result = []
        for operation in self.operations:
            if operation.client == client:
                result.append(operation)
        return result

    #  получение операции с конкретного устройства (terminal)
    def operations_by_terminal(self, terminal: str) -> list[Operation]:
        result = []
        for operation in self.operations:
            if operation.terminal == terminal:
                result.append(operation)
        return result

    #  проверка на множество кликов с одного ID
    def many_clicks(self) -> list[Operation]:
        acceracy = timedelta(minutes=5)  # промежуток времени в 5 минут
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
    def equal_delay(self) -> list[Operation]:
        acceracy = timedelta(seconds=1)  # погрешность в 1 секунду
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
    def day_time(self) -> list[Operation]:
        return list(filter(lambda x: x.date.hour < 6 or x.date.hour > 22, self.operations))
