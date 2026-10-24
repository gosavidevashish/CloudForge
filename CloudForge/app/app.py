import os
from flask import Flask, jsonify
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)

# Prometheus metrics instrumentation
metrics = PrometheusMetrics(app)
metrics.info("app_info", "Application info", version="1.0.0")

# Primary application route
@app.route("/")
def hello():
    return jsonify({"message": "Hello from CloudForge!"}), 200

# Error simulation route (used for testing 404 metrics)
@app.route("/fail")
def fail():
    return jsonify({"error": "Resource not found"}), 404

# --- Health Check Endpoints ---
@app.route("/health", methods=["GET"])
@app.route("/healthz", methods=["GET"])
def healthz():
    """Liveness probe & general health check."""
    return jsonify({"status": "healthy"}), 200

@app.route("/readyz", methods=["GET"])
def readyz():
    """Readiness probe: confirms the app is ready to serve traffic."""
    return jsonify({"status": "ready"}), 200

if __name__ == "__main__":
    host = os.getenv("FLASK_HOST", "0.0.0.0")
    port = int(os.getenv("FLASK_PORT", 5000))
    # nosemgrep: python.flask.security.audit.app-run-param-config.avoid_app_run_with_bad_host
    app.run(host=host, port=port)