\# VERDICT

\### Evidence-First Candidate Evaluation Network



> "PitchBook indexes what's already public. VERDICT indexes what's being ignored."



Built for the \*\*Band of Agents Hackathon\*\* (lablab.ai, June 12–19 2026) by \*\*Null Pointer\*\*.



\---



\## The Problem



Capable candidates get rejected by broken evaluation systems that reward presentation over substance. No feedback. No transparency. No accountability. Just silence.



VERDICT fixes that.



\---



\## What It Does



VERDICT is a multi-agent system where four specialized AI agents collaborate through Band to evaluate candidates — and force every decision to be grounded in documented evidence.



No silent rejections. No vague criteria. Every verdict is traceable.



\---



\## The Agents



| Agent | Role |

|-------|------|

| Evidence Extractor | Parses the candidate profile for verifiable, concrete evidence of capability |

| Criteria Mapper | Scores evidence against explicit role requirements with justification per criterion |

| Bias Auditor | Flags irrelevant evaluation factors — geography, prestige, GPA rigidity |

| Accountability Agent | Generates a mandatory structured verdict with full evidence citations and candidate feedback |



All four agents communicate and hand off context through \*\*Band\*\*.



\---



\## Tracks Covered



\- \*\*Track 1\*\* — Internal Enterprise: corporate hiring pipelines

\- \*\*Track 2\*\* — Multi-Agent Software Dev: automated screening audit tools

\- \*\*Track 3\*\* — Regulated Workflows: research program admissions



\---



\## Stack



\- \*\*Backend\*\*: Flask + LangGraph

\- \*\*Agents\*\*: LangChain + Groq (Llama 3.3 70B)

\- \*\*Agent Comms\*\*: Band REST API

\- \*\*Frontend\*\*: HTML + Tailwind CSS (single-page app)



\---



\## How to Run



```bash

\# Clone the repo

git clone https://github.com/azlaan428/verdict.git

cd verdict



\# Create and activate venv

python -m venv venv

venv\\Scripts\\activate



\# Install dependencies

pip install flask flask-cors langgraph langchain-groq python-dotenv requests



\# Add your keys to .env

GROQ\_API\_KEY=your\_key

BAND\_API\_KEY=your\_key

BAND\_AGENT\_KEY=your\_key

BAND\_ROOM\_ID=your\_room\_id

BAND\_WS\_URL=wss://app.band.ai/api/v1/socket/websocket

BAND\_REST\_URL=https://app.band.ai



\# Run

python app.py

```



Open `http://127.0.0.1:5000` in your browser.



\---



\## Team



\*\*Null Pointer\*\* — Mohammad Azlaan  

Biomedical Engineering, Ziauddin University, Karachi  

Band of Agents Hackathon 2026

