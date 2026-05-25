from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from agents.orchestrator import run_verdict_pipeline
from agents.domain_config import get_domain_labels
from PyPDF2 import PdfReader
from docx import Document
import io

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/domains", methods=["GET"])
def domains():
    return jsonify(get_domain_labels())

@app.route("/evaluate", methods=["POST"])
def evaluate():
    data = request.get_json()
    application_text = data.get("application_text", "")
    role_description = data.get("role_description", "")
    domain = data.get("domain", "research")
    github_username = data.get("github_username", "")
    if not application_text or not role_description:
        return jsonify({"error": "Both application_text and role_description are required"}), 400
    result = run_verdict_pipeline(application_text, role_description, domain, github_username)
    return jsonify(result)

@app.route("/parse-pdf", methods=["POST"])
def parse_pdf():
    if 'pdf' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    file = request.files['pdf']
    filename = file.filename.lower()
    try:
        if filename.endswith('.pdf'):
            reader = PdfReader(io.BytesIO(file.read()))
            text = "\n".join(page.extract_text() or "" for page in reader.pages)
        elif filename.endswith('.docx'):
            doc = Document(io.BytesIO(file.read()))
            text = "\n".join(para.text for para in doc.paragraphs if para.text.strip())
        else:
            return jsonify({"error": "Unsupported file type"}), 400
        return jsonify({"text": text.strip()})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)