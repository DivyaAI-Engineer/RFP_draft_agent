from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware

from src.utils.storage_client import StorageClient
from src.agent.proposal_repository import ProposalRepository
from src.agent.sales_proposal_agent import SalesProposalAgent

app = FastAPI(title="Mobility RFP Draft Proposal Agent")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

_storage_client = StorageClient()
_repo = ProposalRepository(_storage_client)
_agent = SalesProposalAgent(_repo)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/generate-proposal")
async def generate_proposal(rfp_file: UploadFile = File(...)):
    content = await rfp_file.read()
    rfp_text = content.decode("utf-8", errors="ignore")
    draft = _agent.generate_draft(rfp_text)
    return {"proposal": draft}
