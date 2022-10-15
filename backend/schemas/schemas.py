POST_TRANSACTION_SCHEMA = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "type": "object",
    "properties": {
        "date": {
            "type": "string",
            "format": "date-time"
        },
        "card": {"type": "string"},
        "account": {"type": "string"},
        "account_valid_to": {"type": "string"},
        "client": {"type": "string"},
        "last_name": {"type": "string"},
        "first_name": {"type": "string"},
        "patronymic": {"type": "string"},
        "date_of_birth": {"type": "string"},
        "passport": {"type": ["string", "number"]},
        "passport_valid_to": {"type": "string"},
        "phone": {"type": "string"},
        "oper_type": {
            "enum": ["\u041e\u043f\u043b\u0430\u0442\u0430",
                     "\u041f\u043e\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u0435",
                     "\u0421\u043d\u044f\u0442\u0438\u0435"]
        },
        "amount": {"type": "number"},
        "oper_result": {
            "enum": ["\u041e\u0442\u043a\u0430\u0437",
                     "\u0423\u0441\u043f\u0435\u0448\u043d\u043e"]
        },
        "terminal": {"type": "string"},
        "terminal_type": {
            "enum": ["ATM", "POS"]
        },
        "city": {"type": "string"},
        "address": {"type": "string"}
    },
    "required": ["date", "card", "account",
                 "account_valid_to", "client",
                 "last_name", "first_name",
                 "patronymic", "date_of_birth",
                 "passport", "passport_valid_to",
                 "phone", "oper_type", "amount",
                 "oper_result", "terminal",
                 "terminal_type", "city", "address"]
}

FAILED_VALIDATION = {
    "code": 400,
    "message": "Validation Failed"
}