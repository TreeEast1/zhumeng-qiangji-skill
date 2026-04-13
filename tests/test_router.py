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

