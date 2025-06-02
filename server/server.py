from flask import Flask, jsonify
from worldgen import generate_world
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/generate', methods=["GET"])
def home():
    data = generate_world()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)