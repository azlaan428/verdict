\# VERDICT — Status

\## Project

Multi-agent candidate evaluation system built for the Band of Agents Hackathon (lablab.ai, June 12–19 2026).



\## Stack

\- Backend: Flask + LangGraph

\- Agents: LangChain + Groq (Llama 3.3 70B)

\- Agent Comms: Band SDK (REST)

\- Frontend: HTML + Tailwind CSS

\- Infra: Python 3.11, Windows local dev



\## Agents

1\. Evidence Extractor — parses candidate profile for verifiable evidence + GitHub repo scanning

2\. Criteria Mapper — scores evidence against role requirements

3\. Bias Auditor — flags irrelevant evaluation factors

4\. Accountability Agent — generates traceable verdict with candidate feedback



\## Current Status

\- \[x] All 4 agents operational

\- \[x] Band integration posting to room

\- \[x] Flask REST API live

\- \[x] Frontend single-page app connected

\- \[x] Git repo initialized

\- \[x] Multi-domain selector (Research / Corporate / Compliance)

\- \[x] Improvement Roadmap display

\- \[x] Stealth Signal Score (composite: evidence + fit + bias)

\- \[x] Band live feed panel

\- \[x] GitHub repo scanner (live fetch via GitHub API)

\- \[x] PDF upload and auto-parse

\- \[x] DOCX upload and auto-parse

\- \[x] Evidence display cleaned up (no raw JSON)

\- \[x] README updated

\- \[ ] Demo video recorded

\- \[ ] lablab.ai submission form completed



\## Tracks Targeted

\- Track 1: Internal Enterprise (corporate hiring)

\- Track 2: Multi-Agent Software Dev (screening pipeline)

\- Track 3: Regulated Workflows (research program admissions)



\## Live Run Results

\- Domain: Research Program Admission

\- Verdict: WAITLIST (80% confidence)

\- Signal Score: 81/100

\- Bias flags: Geographic bias, GPA rigidity, publication gatekeeping

\- GitHub repos: detected and included in evidence scan

\- Band feed: All 4 agents logged with timestamps



\## Team

Mohammad Azlaan (solo)

