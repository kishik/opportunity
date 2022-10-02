from operation import Operation


def operations_by_client(operations: list[Operation]) -> dict:
    result = {}
    for operation in operations:
        if operation.client not in result:
            result[operation.client] = [operation]
        else:
            result[operation.client].append(operation)
    return result


def many_clicks(operations: list[Operation]) -> list[Operation]:
    pass


def equal_delay(operations: list[Operation]) -> list[Operation]:
    pass


def day_time(operations: list[Operation]) -> list[Operation]:
    return list(filter(lambda x: 6 < x.date.hour < 22, operations))
