from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from agents.orchestrator import run_verdict_pipeline
from agents.domain_config import get_domain_labels

app = Flask(__name__)
CORS(app)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/domains", methods=["GET"])
def domains():
    """Returns available domain options for the frontend selector."""
    return jsonify(get_domain_labels())


@app.route("/evaluate", methods=["POST"])
def evaluate():
    data = request.get_json()

    application_text = data.get("application_text", "")
    role_description = data.get("role_description", "")
    domain = data.get("domain", "research")  # default to research if not provided

    if not application_text or not role_description:
        return jsonify({"error": "Both application_text and role_description are required"}), 400

    result = run_verdict_pipeline(application_text, role_description, domain=domain)
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, port=5000)