from backend.schemas.schemas import POST_TRANSACTION_SCHEMA
import jsonschema

ALLOWED_EXTENSIONS = set(['json'])


class Validate:
    def __init__(self) -> None:
        pass

    def validate_post(self, data: dict) -> bool:
        transactions = data['transactions']
        for transaction in transactions.values():
            try:
                jsonschema.validate(transaction, POST_TRANSACTION_SCHEMA)
            except:
                return False
        return True

    def allowed_file(self, filename: str) -> bool:
        return '.' in filename and \
               filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS
