from flask import Blueprint, jsonify, abort

divide_blueprint = Blueprint('divide', __name__)

@divide_blueprint.route('/divide/<int:numberA>/<int:numberB>', methods=['GET'])
def divide(numberA, numberB):
    if numberB == 0:
        abort(400, description="Division by zero is not allowed.")
    result = numberA / numberB
    return jsonify(status=200, result=result)