from typing import Dict, List


class ConnectivityTool:
    """
    Tool to describe network connectivity options.
    """

    def __init__(self, templates: List[Dict]):
        self.templates = templates

    def generate_connectivity_section(self, parsed_rfp: Dict) -> str:
        base = self.templates[0]["content"] if self.templates else "Standard connectivity model."
        return f"{base}\n\nIncludes carrier options and coverage assumptions."
