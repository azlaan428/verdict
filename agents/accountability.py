import json
from langchain_groq import ChatGroq
from config import GROQ_API_KEY

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    groq_api_key=GROQ_API_KEY,
    temperature=0.2
)


def generate_verdict(
    evidence: dict,
    criteria_scores: dict,
    bias_report: dict,
    role_description: str,
    domain_context: str = ""
) -> dict:
    prompt = f"""
You are an Accountability Agent for a candidate evaluation system.
Your job is to generate a final, fully transparent verdict on a candidate.
Every decision you make must be traceable to specific evidence.
No silent rejections. No vague feedback. Every verdict must be defensible.

{domain_context}

Based on the evidence, criteria scores, and bias report provided, generate:
- verdict: ADVANCE / REJECT / WAITLIST
- confidence: integer 0-100
- decision_rationale: detailed paragraph explaining exactly why this decision was made,
  citing specific evidence from the candidate profile
- evidence_citations: list of specific things from the candidate profile that drove the decision
- bias_adjustments: list of any scoring adjustments made due to bias flags
- feedback_for_candidate: honest, constructive, specific feedback the candidate deserves to receive
  -- not generic, not vague, actionable and respectful
- improvement_roadmap: list of 3 specific things the candidate can do to strengthen
  their profile for future applications

Return a JSON object with all fields above.
Return ONLY valid JSON. No preamble. No explanation.

CANDIDATE EVIDENCE:
{json.dumps(evidence, indent=2)}

CRITERIA SCORES:
{json.dumps(criteria_scores, indent=2)}

BIAS REPORT:
{json.dumps(bias_report, indent=2)}

ROLE DESCRIPTION:
{role_description}
"""
    response = llm.invoke(prompt)
    try:
        clean = response.content.strip().replace("```json", "").replace("```", "").strip()
        return json.loads(clean)
    except Exception as e:
        return {
            "error": str(e),
            "raw_response": response.content,
            "verdict": "ERROR",
            "confidence": 0
        }