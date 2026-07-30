from typing import Dict, List


class MobilePlansTool:
    """
    Tool to describe mobile plans, data bundles, and usage policies.
    """

    def __init__(self, templates: List[Dict]):
        self.templates = templates

    def generate_mobile_plans_section(self, parsed_rfp: Dict) -> str:
        base = self.templates[0]["content"] if self.templates else "Standard mobile plan offering."
        return f"{base}\n\nIncludes data bundles, roaming, and fair use policies."
