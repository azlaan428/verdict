from agents.orchestrator import run_verdict_pipeline

application_text = """
Name: Mohammad Azlaan
Education: Biomedical Engineering, Ziauddin University, CGPA 3.32

Projects:
- ARIA: Multi-agent biomedical literature review system using LangGraph, LangChain, 
  Groq API. Features automated PubMed search, PRISMA screening, evidence synthesis, 
  citation generation. Built for AMD MI300X.
- Depression Screening Tool: ML-based keystroke dynamics classifier using Random Forest. 
  87.5% accuracy. Flask frontend, MySQL backend, 100 participant study ongoing.
- VR Trauma Surgeon Simulator: Unity 6, Meta Quest 3. Built for Microprocessors course.
- ESP32 Drone: PID stabilisation, custom GUI.
- Bio-engineered Air Purifier: Chlorella vulgaris, Pseudomonas putida, 3D printed housing.

Experience:
- Student Team Lead, Biomedical Engineering Department
- Freelance Mathematics Tutor, O-Level and SAT students
- Research supervised by Engr. Taha Mushtaq Shaikh and Engr. Daniyal Alvi

Skills: Python, Flask, LangGraph, LangChain, Unity, MATLAB, Arduino, SQL, React

Hackathons: AMD Developer Hackathon 2026 participant
"""

role_description = """
MITACS Globalink Research Internship
- Strong academic record (GPA 3.5+ preferred)
- Research experience in a relevant field
- Programming skills
- Ability to work independently on a research project
- Strong communication skills
- Evidence of initiative and self-directed learning
"""

result = run_verdict_pipeline(application_text, role_description)

import json
print("\n===== FINAL RESULT =====")
print(json.dumps(result, indent=2))