import asyncio
from agents.band_integration import run_band_pipeline

application_text = """
Name: Mohammad Azlaan
Education: Biomedical Engineering, Ziauddin University, CGPA 3.385
Projects: ARIA multi-agent system, Depression Screening ML tool (87.5% accuracy),
VR Trauma Surgeon Simulator, ESP32 Drone, Bio-engineered Air Purifier.
Skills: Python, Flask, LangGraph, LangChain, Unity, MATLAB, Arduino, SQL, React
Experience: Student Team Lead, Freelance Math Tutor, Research under two supervisors
Hackathons: AMD Developer Hackathon 2026
"""

role_description = """
MITACS Globalink Research Internship
- Strong academic record (GPA 3.5+ preferred)
- Research experience in a relevant field
- Programming skills
- Ability to work independently
- Strong communication skills
"""

result = run_band_pipeline(application_text, role_description)
print("\nVerdict:", result["verdict"]["verdict"])