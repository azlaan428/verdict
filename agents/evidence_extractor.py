import json
import requests
from langchain_groq import ChatGroq
from config import GROQ_API_KEY

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    groq_api_key=GROQ_API_KEY,
    temperature=0.2
)

def fetch_github_data(github_username: str) -> str:
    """Fetch repos and README content from a GitHub username."""
    headers = {"Accept": "application/vnd.github+json"}
    summary = f"GitHub Profile: {github_username}\n\n"

    try:
        # Fetch repos
        res = requests.get(
            f"https://api.github.com/users/{github_username}/repos?sort=updated&per_page=10",
            headers=headers, timeout=10
        )
        if res.status_code != 200:
            return summary + f"[GitHub fetch failed: {res.status_code}]"

        repos = res.json()
        summary += f"Public Repositories ({len(repos)} most recent):\n"

        for repo in repos:
            summary += f"\n--- {repo['name']} ---\n"
            summary += f"Description: {repo.get('description') or 'No description'}\n"
            summary += f"Language: {repo.get('language') or 'Unknown'}\n"
            summary += f"Stars: {repo.get('stargazers_count', 0)} | Forks: {repo.get('forks_count', 0)}\n"
            summary += f"Updated: {repo.get('updated_at', '')[:10]}\n"

            # Try to fetch README
            readme_res = requests.get(
                f"https://api.github.com/repos/{github_username}/{repo['name']}/readme",
                headers={**headers, "Accept": "application/vnd.github.raw"},
                timeout=8
            )
            if readme_res.status_code == 200:
                readme_text = readme_res.text[:800]
                summary += f"README preview:\n{readme_text}\n"

    except Exception as e:
        summary += f"[GitHub fetch error: {e}]\n"

    return summary


def extract_evidence(application_text: str, github_username: str = None) -> dict:
    # If GitHub username provided, enrich application text with repo data
    if github_username and github_username.strip():
        github_data = fetch_github_data(github_username.strip())
        enriched_text = f"{application_text}\n\n--- GITHUB DATA (LIVE) ---\n{github_data}"
    else:
        enriched_text = application_text

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
- github_repos: list of repo names found in GitHub data (empty list if no GitHub data)
- raw_signal_score: integer 0-100 rating the overall strength of evidence found

Return ONLY valid JSON. No preamble. No explanation.

APPLICATION:
{enriched_text}
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