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


def test_guardrail_blocks_weighted_score_mixup():
    result = inspect_answer(
        "这个学校 720 的加权入围成绩是不是就等于裸分 720",
        "是的，加权入围成绩就是高考裸分。",
    )
    assert result["blocked"] is True
    assert any("score_type_mixup" in item for item in result["violations"])


def test_guardrail_blocks_direct_exam_overgeneralization():
    result = inspect_answer(
        "强基是不是所有学校都报名成功直接参加校测",
        "对，所有强基学校都是报名成功就直接进校测。",
    )
    assert result["blocked"] is True
    assert any("pathway_overgeneralization" in item for item in result["violations"])
