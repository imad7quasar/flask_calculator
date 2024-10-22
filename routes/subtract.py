from flask import Blueprint, jsonify

subtract_blueprint = Blueprint('subtract', __name__)

@subtract_blueprint.route('/subtract/<int:numberA>/<int:numberB>', methods=['GET'])
@subtract_blueprint.route('/subtract/<int:numberA>/<int:numberB>', methods=['GET'])
def subtract(numberA, numberB):
    try:
        result = numberA - numberB
        return jsonify(status=200, result=result)
    except Exception as e:
        return jsonify(status=500, error=str(e)), 500
