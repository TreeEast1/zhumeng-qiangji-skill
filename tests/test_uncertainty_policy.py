from zhumeng_qiangji_skill.guardrails import inspect_answer
from zhumeng_qiangji_skill.router import analyze_query


def test_missing_year_triggers_risk_flag():
    result = analyze_query("某校还有强基吗")
    assert "missing_year" in result["risk_flags"]


def test_missing_year_blocks_overconfident_answer():
    result = inspect_answer("某校还有强基吗", "一定有，今年还是老政策。")
    assert result["blocked"] is True
    assert "final_claim_without_year" in result["violations"]

