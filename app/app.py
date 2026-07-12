from flask import Flask

app = Flask(__name__)

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

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)