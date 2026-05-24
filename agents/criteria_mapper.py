import json
from langchain_groq import ChatGroq
from config import GROQ_API_KEY

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    groq_api_key=GROQ_API_KEY,
    temperature=0.2
)

def map_criteria(evidence: dict, role_description: str) -> dict:
    prompt = f"""
You are a Criteria Mapping Agent for a candidate evaluation system.

Your job is to take extracted evidence from a candidate and score it against
the explicit requirements of a role or program.

For each criterion in the role description, assign:
- criterion: the requirement
- evidence_found: what from the candidate's profile supports this
- score: integer 0-10
- justification: one sentence explaining the score

Return a JSON object with:
- criteria_scores: list of criterion objects as described above
- overall_fit_score: integer 0-100 weighted average
- strongest_areas: list of top 3 criteria where candidate excels
- weakest_areas: list of top 3 criteria where candidate falls short

Return ONLY valid JSON. No preamble. No explanation.

CANDIDATE EVIDENCE:
{json.dumps(evidence, indent=2)}

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
            "overall_fit_score": 0
        }