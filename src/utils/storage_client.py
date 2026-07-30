from typing import List, Dict


class StorageClient:
    """
    Simple in-memory stub for proposals/templates.
    Replace with Azure Blob / Cosmos / SQL as needed.
    """

    def __init__(self):
        self._proposals = [
            {"customer_segment": "default", "content": "Previous proposal A"},
            {"customer_segment": "enterprise", "content": "Previous proposal B"},
        ]
        self._templates = {
            "billing": [{"content": "Per-device billing with monthly invoicing."}],
            "connectivity": [{"content": "Multi-carrier connectivity with failover."}],
            "software_updates": [{"content": "OTA updates with staged rollout."}],
            "mobile_plans": [{"content": "Tiered data plans with roaming options."}],
        }

    def list_proposals(self, customer_segment: str) -> List[Dict]:
        return [
            p for p in self._proposals if p["customer_segment"] == customer_segment
        ] or self._proposals

    def list_templates(self, category: str) -> List[Dict]:
        return self._templates.get(category, [])
    
    def get_proposal_repository(self):
        # kept for compatibility if needed
        from src.agent.proposal_repository import ProposalRepository
        return ProposalRepository(self)
