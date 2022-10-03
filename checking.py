'''
Тут хранится класс для проверки операций
'''
from operation import Operation

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
        checked_clients = {}
        temp = None
        for i in range(len(self.operations)):
            if not checked_clients.get(self.operations[i].client):
                client_operation = self.operations_by_client(self.operations[i].client)
                for i in range(1, len(client_operation)):
                    if not temp:
                        pass
    
    # проверка на подозрительную активность в ночное время
    def day_time(self) -> list[Operation]:
        return list(filter(lambda x: 6 < x.date.hour < 22, self.operations))
