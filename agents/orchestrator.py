import json
from agents.evidence_extractor import extract_evidence
from agents.criteria_mapper import map_criteria
from agents.bias_auditor import audit_bias
from agents.accountability import generate_verdict

def run_verdict_pipeline(application_text: str, role_description: str) -> dict:
    print("\n[VERDICT] Starting pipeline...")

    # Stage 1: Evidence Extraction
    print("[Agent 1] Evidence Extractor running...")
    evidence = extract_evidence(application_text)
    print(f"[Agent 1] Done. Signal score: {evidence.get('raw_signal_score', 'N/A')}")

    # Stage 2: Criteria Mapping
    print("[Agent 2] Criteria Mapper running...")
    criteria_scores = map_criteria(evidence, role_description)
    print(f"[Agent 2] Done. Fit score: {criteria_scores.get('overall_fit_score', 'N/A')}")

    # Stage 3: Bias Audit
    print("[Agent 3] Bias Auditor running...")
    bias_report = audit_bias(evidence, criteria_scores)
    print(f"[Agent 3] Done. Bias risk: {bias_report.get('overall_bias_risk', 'N/A')}")

    # Stage 4: Accountability Verdict
    print("[Agent 4] Accountability Agent running...")
    verdict = generate_verdict(evidence, criteria_scores, bias_report, role_description)
    print(f"[Agent 4] Done. Verdict: {verdict.get('verdict', 'N/A')}")

    return {
        "evidence": evidence,
        "criteria_scores": criteria_scores,
        "bias_report": bias_report,
        "verdict": verdict
    }