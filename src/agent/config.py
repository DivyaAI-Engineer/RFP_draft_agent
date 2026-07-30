import os
from dataclasses import dataclass

@dataclass
class AgentConfig:
    azure_openai_endpoint: str = os.getenv("AZURE_OPENAI_ENDPOINT", "")
    azure_openai_deployment: str = os.getenv("AZURE_OPENAI_DEPLOYMENT", "")
    azure_openai_api_key: str = os.getenv("AZURE_OPENAI_API_KEY", "")

    proposals_container: str = os.getenv("PROPOSALS_CONTAINER", "proposals")
    storage_connection_string: str = os.getenv("AZURE_STORAGE_CONNECTION_STRING", "")
