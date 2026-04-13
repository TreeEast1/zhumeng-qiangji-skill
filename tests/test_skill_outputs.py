from zhumeng_qiangji_skill.schemas import validate_payload


def test_answer_schema_validation_passes():
    payload = {
        "summary": "当前信息不足，无法确认最终结论。",
        "question_type": "school_recommendation",
        "route": ["score_type_resolver", "school_recommender", "risk_guard"],
        "conclusion": "由于缺少明确分数类型和可靠证据，暂时不能判断是否能进。",
        "rationale": [
            "用户给出了数字，但未说明是裸分、综合成绩还是位次对应分。",
            "强基计划判断强依赖年份和省份。"
        ],
        "evidence_status": "uncertain",
        "confidence": 0.42,
        "risk_level": "high",
        "next_step": [
            "补充年份、省份和分数类型。",
            "核对目标学校当年官方简章。"
        ],
        "disclaimer": "该结论仅作结构化示例，具体以官方简章为准。"
    }
    validate_payload("answer.schema.json", payload)

