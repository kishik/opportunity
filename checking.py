"""
Тут хранится класс для проверки операций
"""
from operation import Operation
from datetime import datetime, timedelta


class Fraud:
    def __init__(self, operations: list[Operation]) -> None:
        self.operations = operations

    # получение операций от конкретного клиента
    def operations_by_client(self, client: str) -> list[Operation]:
        result = []
        for i in range(len(self.operations)):
            if self.operations[i].client == client:
                result.append(self.operations[i])
        return result

    # проверка на множество кликов с одного ID
    def many_clicks(self) -> list[Operation]:
        pass

    # проверка на одинаковые временные промежутки между операциями
    def equal_delay(self) -> list[Operation]:
        acceracy = timedelta(seconds=1)  #  погрешность в 1 секунду
        checked_clients = {}
        temp = None
        fraud_operations = []
        for i in range(len(self.operations)):
            if not checked_clients.get(self.operations[i].client):
                client_operation = self.operations_by_client(self.operations[i].client)
                for i in range(1, len(client_operation)):
                    if not temp:
                        temp = client_operation[i].date - client_operation[i-1].date
                    else:
                        div = client_operation[i].date - client_operation[i-1].date
                        if div == temp or div == temp + acceracy or div == temp - acceracy:
                            fraud_operations.append(client_operation[i])
                        temp = div
                checked_clients[self.operations[i].client] = 1
        return fraud_operations

    # проверка на подозрительную активность в ночное время
    def day_time(self) -> list[Operation]:
        return list(filter(lambda x: 6 < x.date.hour < 22, self.operations))
