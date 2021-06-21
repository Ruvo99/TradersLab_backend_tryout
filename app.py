from flask import Flask, json, jsonify

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def index():
    return jsonify({'greetings': 'Hi! This came from Python'})

if __name__ == "__main__":
    app.run(debug=True)
