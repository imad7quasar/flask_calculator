from flask import Flask, jsonify
from routes.add import add_blueprint
from routes.subtract import subtract_blueprint
from routes.multiply import multiply_blueprint
from routes.divide import divide_blueprint

app = Flask(__name__)

# Register blueprints
app.register_blueprint(add_blueprint)
app.register_blueprint(subtract_blueprint)
app.register_blueprint(multiply_blueprint)
app.register_blueprint(divide_blueprint)

# Add a root route
@app.route('/')
def home():
    return jsonify(message="Welcome to the calculator API!"), 200

@app.errorhandler(400)
def bad_request(error):
    return jsonify(status=400, error=str(error.description)), 400

if __name__ == '__main__':
    app.run(debug=True)
