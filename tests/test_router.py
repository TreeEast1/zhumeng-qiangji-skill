from zhumeng_qiangji_skill.router import analyze_query


def test_router_detects_score_route():
    result = analyze_query("江苏考生，2026 届，某校 680 能进吗")
    assert "score_type_resolver" in result["recommended_skills"]
    assert "school_recommender" in result["recommended_skills"]
    assert "risk_guard" in result["recommended_skills"]


def test_router_detects_service_route():
    result = analyze_query("我现在该先做政策梳理还是直接冲校测")
    assert "service_router" in result["recommended_skills"]
    assert "exam_prep_advisor" in result["recommended_skills"]


def test_router_detects_direct_exam_pathway_question():
    result = analyze_query("复交南模式是不是报名成功就能直接参加校测")
    assert "school_mode_classifier" in result["recommended_skills"]
    assert "policy_parser" in result["recommended_skills"]


def test_router_detects_interview_only_strategy_query():
    result = analyze_query("我不太擅长笔试，但表达还可以，有哪些只考面试的强基院校值得关注")
    assert "school_recommender" in result["recommended_skills"]
    assert "exam_prep_advisor" in result["recommended_skills"]
