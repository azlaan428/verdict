from flask import Flask, request, jsonify, render_template
from agents.orchestrator import run_verdict_pipeline

app = Flask(__name__)
from flask_cors import CORS
CORS(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/evaluate", methods=["POST"])
def evaluate():
    data = request.get_json()
    
    application_text = data.get("application_text", "")
    role_description = data.get("role_description", "")
    
    if not application_text or not role_description:
        return jsonify({"error": "Both application_text and role_description are required"}), 400
    
    result = run_verdict_pipeline(application_text, role_description)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True, port=5000)