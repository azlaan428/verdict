from config import BAND_API_KEY, BAND_REST_URL, BAND_ROOM_ID, BAND_AGENT_KEY
import json
import requests
from config import BAND_API_KEY, BAND_REST_URL, BAND_ROOM_ID

def post_to_band(agent_id: str, payload: dict, event_type: str = "tool_result"):
    url = f"{BAND_REST_URL}/api/v1/agent/chats/{BAND_ROOM_ID}/events"
    headers = {
        "X-API-Key": BAND_AGENT_KEY,
        "Content-Type": "application/json"
    }
    body = {
        "event": {
            "content": f"[{agent_id}] completed processing",
            "message_type": event_type,
            "metadata": payload
        }
    }
    try:
        response = requests.post(url, headers=headers, json=body, timeout=10)
        if response.status_code in [200, 201]:
            print(f"[Band] {agent_id} posted event successfully")
        else:
            print(f"[Band] {agent_id} post returned {response.status_code}: {response.text}")
    except Exception as e:
        print(f"[Band] {agent_id} post failed: {e}")


def run_band_pipeline(application_text: str, role_description: str) -> dict:
    from agents.evidence_extractor import extract_evidence
    from agents.criteria_mapper import map_criteria
    from agents.bias_auditor import audit_bias
    from agents.accountability import generate_verdict

    print("\n[VERDICT + Band] Starting pipeline...")

    evidence = extract_evidence(application_text)
    post_to_band("evidence-extractor", evidence, "tool_result")

    criteria_scores = map_criteria(evidence, role_description)
    post_to_band("criteria-mapper", criteria_scores, "tool_result")

    bias_report = audit_bias(evidence, criteria_scores)
    post_to_band("bias-auditor", bias_report, "tool_result")

    verdict = generate_verdict(evidence, criteria_scores, bias_report, role_description)
    post_to_band("accountability-agent", verdict, "tool_result")

    return {
        "evidence": evidence,
        "criteria_scores": criteria_scores,
        "bias_report": bias_report,
        "verdict": verdict
    }