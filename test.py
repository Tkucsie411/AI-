from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Hello, Flask with Gunicorn!"})

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
