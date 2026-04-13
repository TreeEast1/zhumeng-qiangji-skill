from zhumeng_qiangji_skill.guardrails import inspect_answer


def test_guardrail_blocks_composite_score_mixup():
    result = inspect_answer("综合成绩 780 算什么水平", "这基本就是 780 裸分。")
    assert result["blocked"] is True
    assert any("score_type_mixup" in item for item in result["violations"])


def test_guardrail_blocks_uniform_shortlist_claim():
    result = inspect_answer(
        "复交南模式学校是不是都有统一入围线",
        "是的，复交南模式学校都有统一入围线。",
    )
    assert result["blocked"] is True
    assert any("mode_mixup" in item for item in result["violations"])

