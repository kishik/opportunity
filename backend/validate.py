from backend.schemas.schemas import POST_TRANSACTION_SCHEMA
import jsonschema


def validate_post(data: dict) -> bool:
    transactions = data['transactions']
    for transaction in transactions.values():
        try:
            jsonschema.validate(transaction, POST_TRANSACTION_SCHEMA)
        except:
            return False
    return True
