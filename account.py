from backend.transaction import Operation


# TODO создать общего предка для классов аккаунт и клиент и унаследовать их от него
# TODO у клиента может быть несколько аккаунтов по идее
# TODO у клиента и аккаунта мног транзакций

# TODO добавить проверку покупки в городе 2 после недавней покупки в городе 1 (1 час например)
# TODO мб блокирвку по разным адресам в течение 1 минуты
class Account:

    def __init__(self, account_id: str, operation: Operation):
        self.id = account_id
        self.operations = [operation]

    @property
    def number_of_transactions(self) -> int:
        return len(self.operations)

    @property
    def average_transaction(self) -> float:
        return sum(operation.amount for operation in self.operations) / self.number_of_transactions

    @property
    def time_of_transactions(self) -> tuple:
        return tuple(operation.date for operation in self.operations)

    @property
    def frequency_of_transactions(self):
        time = {}
        for operation in self.operations:
            if operation.date.hour in time:
                time[operation.date.hour] += 1
            else:
                time[operation.date.hour] = 1
        return time

    @property
    def results_of_operations(self):
        return tuple(operation.oper_result for operation in self.operations)

    @property
    def frequency_of_results(self):
        result = {}
        for operation in self.operations:
            if operation.oper_result in result:
                result[operation.oper_result] += 1
            else:
                result[operation.oper_result] = 1
        return result

    @property
    def addresses_of_cities(self):
        return tuple(operation.city for operation in self.operations)

    @property
    def frequency_of_cities(self):
        cities = {}
        for operation in self.operations:
            if operation.city in cities:
                cities[operation.city] += 1
            else:
                cities[operation.city] = 1
        return cities

    @property
    def addresses_of_transactions(self):
        return tuple(operation.address for operation in self.operations)

    @property
    def frequency_of_addresses(self):
        addresses = {}
        for operation in self.operations:
            if operation.address in addresses:
                addresses[operation.address] += 1
            else:
                addresses[operation.address] = 1
        return addresses

    @property
    def max_transaction(self):
        return max(tuple(operation.amount for operation in self.operations))

    def add_operation(self, operation):
        self.operations.append(operation)
