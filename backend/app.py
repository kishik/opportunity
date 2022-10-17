import json
import os

from werkzeug.utils import secure_filename
from flask import Flask, jsonify, request
from backend.validate import Validate
from backend.helper import Helper, get_fraud_transactions
from backend.schemas.schemas import FAILED_VALIDATION

UPLOAD_FOLDER = 'backend/uploads'

app = Flask('FraudAPI')
app.config['JSON_AS_ASCII'] = False
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
v = Validate()
h = Helper()


@app.route('/import_transactions', methods=['POST'])
def import_transations():
    file = request.files.get('file')
    if file:
        if not v.allowed_file(file.filename):
            return jsonify(FAILED_VALIDATION), 400
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        with open(filename, 'r') as f:
            data = json.loads(f.read())
    else:
        data = request.get_json()
    if v.validate_post(data):
        h.add_transactions_to_db(data)
        return jsonify(get_fraud_transactions(data)), 200
    return jsonify(FAILED_VALIDATION), 400


@app.route('/get_transactions', methods=['GET'])
def get_transactions():
    return jsonify(h.get_all_transactions()), 200


@app.route('/get_cities', methods=['GET'])
def get_cities():
    return jsonify(h.get_all_cities()), 200


@app.route('/get_transactions/<string:transactions>', methods=['GET'])
def get_transactions(transactions: str):
    return jsonify(h.get_transactions_data(transactions)), 200


if __name__ == '__main__':
    app.run()
