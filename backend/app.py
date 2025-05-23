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

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)