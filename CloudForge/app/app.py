import os
from flask import Flask, jsonify
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)

# Initialize metrics exporter
metrics = PrometheusMetrics(app)
metrics.info('app_info', 'Application information', version='1.0.0')

@app.route("/")
def home():
    return jsonify({
        "status": "success",
        "message": "DevSecOps Pipeline Running Successfully",
        "environment": os.getenv("ENVIRONMENT", "development")
    })

@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    host = os.getenv("HOST", "0.0.0.0")
    # nosemgrep: python.flask.security.audit.app-run-param-config.avoid_app_run_with_bad_host
    app.run(host=host, port=port)