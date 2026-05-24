import json
from langchain_groq import ChatGroq
from config import GROQ_API_KEY

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    groq_api_key=GROQ_API_KEY,
    temperature=0.2
)

def extract_evidence(application_text: str) -> dict:
    prompt = f"""
You are an Evidence Extraction Agent for a candidate evaluation system.

Your job is to extract ONLY concrete, verifiable evidence of capability from the application below.
Do not make assumptions. Do not infer. Only extract what is explicitly stated.

Extract and return a JSON object with these fields:
- projects: list of projects with name, description, tech stack, and measurable impact
- publications: list of papers or research with title, venue, and status
- skills: list of technical skills with proficiency level (beginner/intermediate/advanced)
- experience: list of roles or positions with organization, duration, and responsibilities
- achievements: list of awards, hackathon placements, certifications
- education: degree, institution, GPA if mentioned
- raw_signal_score: integer 0-100 rating the overall strength of evidence found

Return ONLY valid JSON. No preamble. No explanation.

APPLICATION:
{application_text}
"""
    response = llm.invoke(prompt)
    
    try:
        clean = response.content.strip().replace("```json", "").replace("```", "").strip()
        return json.loads(clean)
    except Exception as e:
        return {
            "error": str(e),
            "raw_response": response.content,
            "raw_signal_score": 0
        }