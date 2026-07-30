from typing import List, Dict


class ProposalRepository:
    """
    Repository abstraction for previous proposals/templates.
    Backed by StorageClient (Blob, DB, etc.).
    """

    def __init__(self, storage_client):
        self.storage_client = storage_client

    def list_previous_proposals(self, customer_segment: str) -> List[Dict]:
        return self.storage_client.list_proposals(customer_segment)

    def get_billing_templates(self) -> List[Dict]:
        return self.storage_client.list_templates("billing")

    def get_connectivity_templates(self) -> List[Dict]:
        return self.storage_client.list_templates("connectivity")

    def get_software_update_templates(self) -> List[Dict]:
        return self.storage_client.list_templates("software_updates")

    def get_mobile_plans_templates(self) -> List[Dict]:
        return self.storage_client.list_templates("mobile_plans")
