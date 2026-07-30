from pydantic import BaseModel
from typing import List


class RFPModel(BaseModel):
    raw_text: str
    requirements: List[str]
    timeline: str
    customer_segment: str = "default"
