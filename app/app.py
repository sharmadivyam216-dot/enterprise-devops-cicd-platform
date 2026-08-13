from flask import Flask
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
from time import time

app = Flask(__name__)

# Prometheus Metrics
REQUEST_COUNT = Counter(
    "flask_http_request_total",
    "Total number of HTTP requests"
)

REQUEST_LATENCY = Histogram(
    "flask_http_request_duration_seconds",
    "HTTP request latency"
)


@app.before_request
def before_request():
    app.start_time = time()


@app.after_request
def after_request(response):
    REQUEST_COUNT.inc()
    REQUEST_LATENCY.observe(time() - app.start_time)
    return response


@app.route("/")
def home():
    return """
    <h1>Enterprise DevOps CI/CD Platform</h1>
    <h3>🚀 Successfully deployed using Jenkins, Docker, Kubernetes & AWS</h3>
    """


@app.route("/health")
def health():
    return {
        "status": "UP"
    }


@app.route("/metrics")
def metrics():
    return generate_latest(), 200, {
        "Content-Type": CONTENT_TYPE_LATEST
    }


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)