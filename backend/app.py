from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

counter = 0

@app.route('/hit')
def hit():
    global counter
    counter += 1
    return jsonify({"count": counter})