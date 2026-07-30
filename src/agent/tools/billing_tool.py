from typing import Dict, List


class BillingTool:
    """
    Tool to suggest billing structures based on templates and RFP requirements.
    """

    def __init__(self, templates: List[Dict]):
        self.templates = templates

    def generate_billing_section(self, parsed_rfp: Dict) -> str:
        # Placeholder: pick first template and adapt.
        base = self.templates[0]["content"] if self.templates else "Standard billing model."
        return f"{base}\n\nAligned to requirements: {len(parsed_rfp.get('requirements', []))} items."
