from typing import Any

from src.agent.config import AgentConfig


class DummyLLMClient:
    """
    Placeholder client simulating Azure AI Foundry / Azure OpenAI.
    Replace with actual SDK (azure-ai-inference, etc.).
    """

    def complete(self, messages, temperature: float = 0.2) -> Any:
        class Msg:
            def __init__(self, content):
                self.content = content

        class Choice:
            def __init__(self, content):
                self.message = Msg(content)

        class Response:
            def __init__(self, content):
                self.choices = [Choice(content)]

        # Very simple echo-style stub.
        return Response(
            "{"  # pretend JSON
            '"executive_summary": "Draft executive summary...",'
            '"solution_overview": "Draft solution overview...",'
            '"imei_management": "IMEI management section...",'
            '"software_updates": "Software updates section...",'
            '"connectivity": "Connectivity section...",'
            '"mobile_plans": "Mobile plans section...",'
            '"billing_model": "Billing model section...",'
            '"timeline": "Timeline section...",'
            '"sla_support": "SLA support section...",'
            '"risks_assumptions": "Risks and assumptions section..."'
            "}"
        )


def get_llm_client() -> DummyLLMClient:
    # In real code, use AgentConfig + Azure credentials to build a proper client.
    _ = AgentConfig()  # just to show usage
    return DummyLLMClient()
