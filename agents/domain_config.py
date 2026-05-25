DOMAIN_CONFIGS = {
    "research": {
        "label": "Research Program Admission",
        "criteria_context": """
You are evaluating a candidate for a RESEARCH PROGRAM (e.g. MITACS, KAUST VSRP, MBZUAI UGRIP, INSAIT).
Weight these criteria heavily:
- Research experience and output (publications, theses, lab work)
- Technical depth in a specific domain
- Independent thinking and problem-solving ability
- Academic record and GPA (but not as a hard cutoff)
- Communication and writing ability
- Alignment between candidate interests and program focus
De-weight or ignore:
- Industry work experience unless directly research-relevant
- Business or entrepreneurship experience
- Non-technical achievements
""",
        "bias_context": """
You are auditing bias in a RESEARCH PROGRAM evaluation.
Pay special attention to these bias types specific to research admissions:
- Geographic bias: systematic undervaluation of candidates from South Asia, Africa, or MENA
- Institutional prestige bias: favoring MIT/Stanford alumni over equally capable candidates from regional universities
- Publication gatekeeping: requiring peer-reviewed publications from candidates who are still undergraduates
- GPA cutoff rigidity: hard GPA thresholds that ignore exceptional project output or research contributions
- Language bias: penalizing non-native English speakers in written applications
- Network bias: favoring candidates with pre-existing connections to faculty
""",
        "verdict_context": """
You are generating a verdict for a RESEARCH PROGRAM application.
Your feedback must be specific to academic and research growth.
Improvement roadmap items should focus on:
- Building a research portfolio
- Publishing or pre-printing work
- Strengthening faculty connections
- Improving GPA if it is a hard barrier
- Targeting better-fit programs based on research alignment
Tone: honest, academic, respectful. The candidate is a student trying to grow.
"""
    },

    "corporate": {
        "label": "Corporate Hiring Pipeline",
        "criteria_context": """
You are evaluating a candidate for a CORPORATE ROLE (e.g. software engineer, data scientist, product manager).
Weight these criteria heavily:
- Demonstrated ability to ship working products
- Relevant technical skills matching the job description
- Past work experience and measurable impact
- Collaboration and communication ability
- Problem-solving under constraints
- Portfolio of real projects with outcomes
De-weight or ignore:
- GPA unless the role explicitly requires it
- Academic publications unless directly relevant
- Theoretical knowledge without practical application
""",
        "bias_context": """
You are auditing bias in a CORPORATE HIRING evaluation.
Pay special attention to these bias types specific to corporate hiring:
- Geographic bias: penalizing candidates from non-Western countries without justification
- Employment gap bias: penalizing candidates for career gaps without investigating reasons
- Credential inflation: requiring degrees for roles that do not need them
- Age or experience recency bias: penalizing candidates whose experience is not from the last 2 years
- University prestige bias: filtering by university ranking instead of demonstrated skill
- Affinity bias: favoring candidates who attended the same schools as the hiring team
""",
        "verdict_context": """
You are generating a verdict for a CORPORATE HIRING decision.
Your feedback must be practical and career-focused.
Improvement roadmap items should focus on:
- Building or improving a portfolio of shipped projects
- Gaining specific technical certifications if required
- Targeting roles that better match current experience level
- Improving how experience is framed and communicated
Tone: direct, professional, constructive. The candidate needs actionable career advice.
"""
    },

    "compliance": {
        "label": "Compliance & Regulatory Screening",
        "criteria_context": """
You are evaluating a candidate or document for a COMPLIANCE OR REGULATORY WORKFLOW
(e.g. financial loan application, regulatory approval, credential verification).
Weight these criteria heavily:
- Completeness and accuracy of submitted documentation
- Meeting minimum regulatory or eligibility thresholds
- Risk indicators or red flags in the submission
- Verification of claimed credentials or qualifications
- Consistency between different parts of the submission
De-weight or ignore:
- Subjective impressions of quality
- Factors not listed in the compliance criteria
- Information not present in the submission
""",
        "bias_context": """
You are auditing bias in a COMPLIANCE SCREENING evaluation.
Pay special attention to these bias types specific to compliance:
- Geographic risk profiling: flagging submissions from certain countries without case-specific evidence
- Name or identity bias: differential treatment based on applicant name or demographic inference
- Documentation bias: penalizing applicants who cannot produce documentation due to systemic barriers
- Income or collateral bias: applying wealth-based criteria to non-financial eligibility decisions
- Recency bias: over-weighting recent negative indicators while ignoring long positive history
""",
        "verdict_context": """
You are generating a verdict for a COMPLIANCE SCREENING decision.
Your feedback must be regulatory and process-focused.
Improvement roadmap items should focus on:
- Completing missing documentation
- Resolving flagged inconsistencies
- Meeting specific threshold requirements
- Reapplying after addressing compliance gaps
Tone: formal, precise, neutral. This is a regulatory context.
"""
    }
}


def get_domain_config(domain: str) -> dict:
    """
    Returns the domain config for the given domain key.
    Falls back to research if domain is unknown.
    """
    return DOMAIN_CONFIGS.get(domain, DOMAIN_CONFIGS["research"])


def get_domain_labels() -> dict:
    """
    Returns a dict of domain_key -> label for frontend display.
    """
    return {k: v["label"] for k, v in DOMAIN_CONFIGS.items()}