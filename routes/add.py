from flask import Blueprint, request, jsonify

add_blueprint = Blueprint('add', __name__)

@add_blueprint.route('/add', methods=['GET'])
def add():
    try:
        a = float(request.args.get('a'))
        b = float(request.args.get('b'))
        result = a + b
        return jsonify(result=result)
    except (TypeError, ValueError):
        return jsonify(error="Invalid input"), 400
