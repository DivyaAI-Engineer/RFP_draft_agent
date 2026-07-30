from src.agent.sales_proposal_agent import SalesProposalAgent
from src.utils.storage_client import StorageClient
from src.agent.proposal_repository import ProposalRepository


def test_sales_proposal_agent_generates_draft():
    storage = StorageClient()
    repo = ProposalRepository(storage)
    agent = SalesProposalAgent(repo)

    rfp_text = "RFP requires IMEI tracking and monthly billing."
    draft = agent.generate_draft(rfp_text)

    assert "raw_llm_output" in draft
    assert "executive_summary" in draft["raw_llm_output"]
