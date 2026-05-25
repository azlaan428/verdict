# VERDICT
### Evidence-First Candidate Evaluation Network

> *"The system that should have existed. Built by someone it failed."*

Built for the **Band of Agents Hackathon** (lablab.ai, June 12–19 2026) by **Mohammad Azlaan**.

---

## The Problem

Capable candidates get rejected by broken evaluation systems that reward presentation over substance. No feedback. No transparency. No accountability. Just silence.

VERDICT fixes that — by forcing every selection decision to be grounded in documented evidence, auditable for bias, and traceable to specific reasoning.

---

## What It Does

VERDICT is a multi-agent system where four specialized AI agents collaborate through **Band** to evaluate candidates across three domains: research program admissions, corporate hiring, and compliance screening.

Each agent processes the candidate profile in sequence, posts its output to a Band room, and hands off to the next. The result is a structured verdict with full evidence citations, bias flags, candidate feedback, and an improvement roadmap — not silence.

---

## The Agents

| Agent | Role |
|-------|------|
| **Evidence Extractor** | Parses the candidate profile for verifiable, concrete evidence of capability — projects, skills, experience, achievements |
| **Criteria Mapper** | Scores evidence against explicit role requirements with per-criterion justification and an overall fit score |
| **Bias Auditor** | Flags irrelevant evaluation factors — geographic bias, institutional prestige bias, GPA cutoff rigidity, publication gatekeeping |
| **Accountability Agent** | Generates a mandatory structured verdict (ADVANCE / WAITLIST / REJECT) with full evidence citations, candidate feedback, and improvement roadmap |

All four agents communicate and hand off context through **Band** in real time.

---

## Live Demo Output (Real Run)

- **Domain**: Research Program Admission
- **Candidate**: Biomedical Engineering undergraduate, CGPA 3.385, 6 projects including multi-agent systems
- **Role**: MITACS Globalink Research Internship
- **Verdict**: WAITLIST — 80% confidence
- **Bias flags caught**: Geographic bias (Ziauddin University undervalued), GPA cutoff rigidity, publication gatekeeping for an undergraduate
- **Signal Score**: 70/100
- **Band feed**: All four agents logged in sequence with timestamps

---

## Tracks Covered

- **Track 1** — Internal Enterprise: corporate hiring pipelines
- **Track 2** — Multi-Agent Software Dev: automated screening audit tools  
- **Track 3** — Regulated Workflows: research program admissions

---

## Stack

| Layer | Technology |
|-------|-----------|
| Backend | Flask + LangGraph |
| Agents | LangChain + Groq (Llama 3.3 70B) |
| Agent Comms | Band REST API |
| Frontend | HTML + Tailwind CSS (single-page app) |
| Infra | Python 3.11, Windows local dev |

---

## How to Run

```bash
# Clone the repo
git clone https://github.com/azlaan428/verdict.git
cd verdict

# Create and activate venv
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install flask flask-cors langgraph langchain-groq python-dotenv requests

# Add your keys to .env
GROQ_API_KEY=your_key
BAND_API_KEY=your_key
BAND_AGENT_KEY=your_agent_key
BAND_ROOM_ID=your_room_id
BAND_WS_URL=wss://app.band.ai/api/v1/socket/websocket
BAND_REST_URL=https://app.band.ai

# Run
python app.py
```

Open `http://127.0.0.1:5000` in your browser.

---

## Project Structure

```
verdict/
├── app.py                        # Flask API
├── config.py                     # Environment config
├── agents/
│   ├── domain_config.py          # Multi-domain prompt injections
│   ├── orchestrator.py           # Pipeline coordinator
│   ├── evidence_extractor.py
│   ├── criteria_mapper.py
│   ├── bias_auditor.py
│   ├── accountability.py
│   └── band_integration.py       # Band REST posting
├── templates/
│   └── index.html                # Single-page frontend
└── .env
```

---

## Why This Exists

This system was built because the current evaluation process failed someone who deserved better. Multiple rejections from MITACS, INSAIT, KAUST, MBZUAI, GIST, and DGIST — with no feedback, no criteria, no rationale. Just silence.

VERDICT is the system that should have existed. It cannot give back what was lost. But it can make sure the next candidate gets an answer they can actually use.

---

## Team

**Mohammad Azlaan**  
Biomedical Engineering, Ziauddin University, Karachi  
Band of Agents Hackathon 2026