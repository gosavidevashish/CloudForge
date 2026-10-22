import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health():
    return jsonify({
        "status": "healthy",
        "environment": os.getenv("ENVIRONMENT", "unknown"),
        "version": os.getenv("APP_VERSION", "1.0.0")
    }), 200

@app.route('/', methods=['GET'])
def index():
    return jsonify({
        "message": "DevOps Demo App Running on Kubernetes!",
        "status": "active"
    }), 200

if __name__ == '__main__':
    port = int(os.getenv("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
