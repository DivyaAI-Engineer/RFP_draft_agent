from typing import Dict, List


class RFPParser:
    """
    Very simple RFP parser stub.
    In a real system, LLM-assisted extraction or Prompt Flow is used
    """

    def parse(self, rfp_text: str) -> Dict:
        # Naive section extraction by keywords (placeholder).
        lines = rfp_text.splitlines()
        requirements: List[str] = [l for l in lines if "require" in l.lower()]
        timeline = next((l for l in lines if "timeline" in l.lower()), "")

        return {
            "raw_text": rfp_text,
            "requirements": requirements,
            "timeline": timeline,
            "customer_segment": "default",
        }
