from typing import Dict, Any

from src.agent.rfp_parser import RFPParser
from src.agent.proposal_repository import ProposalRepository
from src.agent.tools.billing_tool import BillingTool
from src.agent.tools.connectivity_tool import ConnectivityTool
from src.agent.tools.software_update_tool import SoftwareUpdateTool
from src.agent.tools.mobile_plans_tool import MobilePlansTool
from src.utils.azure_foundry_client import get_llm_client


class SalesProposalAgent:
    """
    Orchestrates parsing, repository lookup, tools, and LLM to produce a draft proposal.
    """

    def __init__(self, repo: ProposalRepository):
        self.repo = repo
        self.parser = RFPParser()
        self.llm = get_llm_client()

    def _build_tools(self, parsed_rfp: Dict):
        billing_templates = self.repo.get_billing_templates()
        connectivity_templates = self.repo.get_connectivity_templates()
        sw_templates = self.repo.get_software_update_templates()
        plans_templates = self.repo.get_mobile_plans_templates()

        return {
            "billing": BillingTool(billing_templates),
            "connectivity": ConnectivityTool(connectivity_templates),
            "software_updates": SoftwareUpdateTool(sw_templates),
            "mobile_plans": MobilePlansTool(plans_templates),
        }

    def generate_draft(self, rfp_text: str) -> Dict[str, Any]:
        parsed = self.parser.parse(rfp_text)
        previous = self.repo.list_previous_proposals(parsed.get("customer_segment", "default"))
        tools = self._build_tools(parsed)

        billing_section = tools["billing"].generate_billing_section(parsed)
        connectivity_section = tools["connectivity"].generate_connectivity_section(parsed)
        sw_section = tools["software_updates"].generate_software_updates_section(parsed)
        plans_section = tools["mobile_plans"].generate_mobile_plans_section(parsed)

        system_prompt = (
            "You are a Draft Proposal Agent for a mobility fleet company. "
            "Generate a structured proposal JSON with keys: "
            "executive_summary, solution_overview, imei_management, "
            "software_updates, connectivity, mobile_plans, billing_model, "
            "timeline, sla_support, risks_assumptions."
        )

        user_content = (
            f"RFP:\n{rfp_text}\n\n"
            f"Parsed RFP:\n{parsed}\n\n"
            f"Previous proposals:\n{previous}\n\n"
            f"Pre-generated sections:\n"
            f"Billing:\n{billing_section}\n\n"
            f"Connectivity:\n{connectivity_section}\n\n"
            f"Software updates:\n{sw_section}\n\n"
            f"Mobile plans:\n{plans_section}\n"
        )

        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_content},
        ]

        # Placeholder LLM call; adapt to actual Azure AI Foundry client.
        response = self.llm.complete(messages=messages, temperature=0.2)
        content = response.choices[0].message.content

        return {"raw_llm_output": content}
