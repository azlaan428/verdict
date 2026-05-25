import json
from langchain_groq import ChatGroq
from config import GROQ_API_KEY

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    groq_api_key=GROQ_API_KEY,
    temperature=0.2
)


def audit_bias(evidence: dict, criteria_scores: dict, domain_context: str = "") -> dict:
    prompt = f"""
You are a Bias Auditor Agent for a candidate evaluation system.
Your job is to detect potential bias in how a candidate is being evaluated.
You must flag any criteria or scoring patterns that correlate with irrelevant factors
rather than actual capability.

{domain_context}

For each bias type found, return:
- bias_type: name of the bias
- severity: low / medium / high
- evidence: what triggered this flag
- recommendation: how to correct it

Return a JSON object with:
- bias_flags: list of bias objects as described above
- overall_bias_risk: low / medium / high
- bias_risk_score: integer 0-100 where 100 is maximum bias risk
- summary: one paragraph explaining the overall bias assessment

Return ONLY valid JSON. No preamble. No explanation.

CANDIDATE EVIDENCE:
{json.dumps(evidence, indent=2)}

CRITERIA SCORES:
{json.dumps(criteria_scores, indent=2)}
"""
    response = llm.invoke(prompt)
    try:
        clean = response.content.strip().replace("```json", "").replace("```", "").strip()
        return json.loads(clean)
    except Exception as e:
        return {
            "error": str(e),
            "raw_response": response.content,
            "overall_bias_risk": "unknown",
            "bias_risk_score": 0
        }