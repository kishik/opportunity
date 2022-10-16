import json

from flask import Flask, jsonify, request
from backend.validate import Validate
from backend.helper import Helper, get_fraud_transactions
from backend.schemas.schemas import FAILED_VALIDATION


app = Flask('FraudAPI')
app.config['JSON_AS_ASCII'] = False
v = Validate()
h = Helper()


@app.route('/import_transations', methods=['POST'])
def import_transations():
    file = request.files['file']
    if file:
        if not v.allowed_file(file):
            return jsonify(FAILED_VALIDATION), 400
        with open(file, 'r') as f:
            data = json.loads(f.read())
    else:
        data = request.get_json()
    if v.validate_post(data):
        return jsonify(get_fraud_transactions(data)), 200
    return jsonify(FAILED_VALIDATION), 400


if __name__ == '__main__':
    app.run()
