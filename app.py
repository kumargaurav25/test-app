from flask import Flask, jsonify, send_from_directory

app = Flask(__name__, static_folder="static")

@app.route("/")
def root():
    return send_from_directory(app.static_folder, "index.html")

@app.route("/api/message")
def message():
    return jsonify({"message": "Hello from backend!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)