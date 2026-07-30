from typing import Dict, List


class SoftwareUpdateTool:
    """
    Tool to describe software update and patch strategy.
    """

    def __init__(self, templates: List[Dict]):
        self.templates = templates

    def generate_software_updates_section(self, parsed_rfp: Dict) -> str:
        base = self.templates[0]["content"] if self.templates else "Standard software update strategy."
        return f"{base}\n\nCovers OTA updates, security patches, and maintenance windows."
