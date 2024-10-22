from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route('/add', methods=['GET'])
def add():
    # Example route for addition
    return jsonify(status=200, result=5+3)

@app.route('/subtract/<int:a>/<int:b>', methods=['GET'])
def subtract(a, b):
    result = a - b
    return jsonify(status=200, result=result)

# Expose the Flask app as Vercel handler
from vercel_wsgi import handle_wsgi
app = handle_wsgi(app)
