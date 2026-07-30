from pydantic import BaseModel


class ProposalModel(BaseModel):
    executive_summary: str
    solution_overview: str
    imei_management: str
    software_updates: str
    connectivity: str
    mobile_plans: str
    billing_model: str
    timeline: str
    sla_support: str
    risks_assumptions: str
