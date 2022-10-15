from flask import Flask, jsonify, request
from backend.validate import validate_post
from backend.schemas.schemas import FAILED_VALIDATION

app = Flask('FraudAPI')


@app.route('/import_transations', methods=['POST'])
def import_transations():
    data = request.get_json()
    if validate_post(data):
        return '', 200
    return jsonify(FAILED_VALIDATION), 400


if __name__ == '__main__':
    app.run()
