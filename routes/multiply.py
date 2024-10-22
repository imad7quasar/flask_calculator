from flask import Blueprint, jsonify

multiply_blueprint = Blueprint('multiply', __name__)

# Define a route that takes two integer parameters from the URL
@multiply_blueprint.route('/multiply/<int:numberA>/<int:numberB>', methods=['GET'])
def multiply(numberA, numberB):
    result = numberA * numberB
    return jsonify(status=200, result=result)
