from src.agent.rfp_parser import RFPParser


def test_rfp_parser_basic():
    parser = RFPParser()
    text = "This RFP requires connectivity.\nTimeline: 6 months."
    parsed = parser.parse(text)
    assert "connectivity" in " ".join(parsed["requirements"]).lower()
    assert "timeline" in parsed["timeline"].lower()
