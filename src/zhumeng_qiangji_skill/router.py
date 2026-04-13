from __future__ import annotations

import re
from typing import Any

from .paths import load_yaml, repo_root

PROVINCES = [
    "北京",
    "天津",
    "河北",
    "山西",
    "内蒙古",
    "辽宁",
    "吉林",
    "黑龙江",
    "上海",
    "江苏",
    "浙江",
    "安徽",
    "福建",
    "江西",
    "山东",
    "河南",
    "湖北",
    "湖南",
    "广东",
    "广西",
    "海南",
    "重庆",
    "四川",
    "贵州",
    "云南",
    "西藏",
    "陕西",
    "甘肃",
    "青海",
    "宁夏",
    "新疆",
]

SUBJECT_PATTERNS = [
    "物化生",
    "物化政",
    "物化地",
    "物生政",
    "物生地",
    "物政地",
    "史政地",
    "史政生",
    "史化生",
    "物化",
    "物生",
    "物政",
]

YEAR_RE = re.compile(r"\b(20\d{2})\b")
SCORE_RE = re.compile(r"(?<!\d)([3-8]\d{2}(?:\.\d)?)(?!\d)")
RANK_RE = re.compile(r"(?:位次|排名)\s*([1-9]\d{0,5})")


def _load_rules() -> dict[str, Any]:
    return load_yaml(repo_root() / "rules" / "routing_rules.yaml")


def _load_mock_school_names() -> list[str]:
    data = load_yaml(repo_root() / "knowledge" / "mock" / "schools.demo.yaml")
    return [item["school_name"] for item in data.get("schools", [])]


def extract_context(raw_query: str) -> dict[str, Any]:
    query = raw_query.strip()
    year_match = YEAR_RE.search(query)
    year = int(year_match.group(1)) if year_match else None

    province = next((p for p in PROVINCES if p in query), None)
    subject_selection = next((s for s in SUBJECT_PATTERNS if s in query), None)

    school_name = None
    for candidate in _load_mock_school_names():
        if candidate in query:
            school_name = candidate
            break

    score = None
    for match in SCORE_RE.finditer(query):
        number = float(match.group(1))
        if year is not None and int(number) == year:
            continue
        score = number
        break

    rank_match = RANK_RE.search(query)
    rank = int(rank_match.group(1)) if rank_match else None

    if "没有竞赛" in query or "无竞赛" in query:
        olympiad_background = "none"
    elif "省赛" in query:
        olympiad_background = "provincial"
    elif "国赛" in query:
        olympiad_background = "national"
    else:
        olympiad_background = None

    return {
        "raw_query": query,
        "year": year,
        "province": province,
        "subject_selection": subject_selection,
        "school_name": school_name,
        "score": score,
        "rank": rank,
        "olympiad_background": olympiad_background,
    }


def infer_score_type(query: str, score: float | None) -> str | None:
    if score is None and not any(term in query for term in ["分", "线", "成绩", "位次"]):
        return None
    if "综合成绩" in query:
        return "composite_score"
    if "裸分" in query:
        return "gaokao_raw_score"
    if "入围线" in query:
        return "shortlist_line"
    if "录取线" in query:
        return "admission_line"
    if "校测" in query or "面试分" in query or "笔试分" in query:
        return "exam_score"
    if "加权" in query:
        return "weighted_score"
    if "位次对应分" in query:
        return "rank_based_estimate"
    if score is not None:
        return "unknown"
    return None


def analyze_query(raw_query: str) -> dict[str, Any]:
    rules = _load_rules()
    context = extract_context(raw_query)
    query = context["raw_query"]
    score_type = infer_score_type(query, context["score"])

    matched_types: list[tuple[str, int]] = []
    recommended_skills: list[str] = []
    rationale: list[str] = []

    for question_type, config in rules["question_types"].items():
        keywords = config.get("keywords", [])
        score = sum(1 for keyword in keywords if keyword in query)
        if score > 0:
            matched_types.append((question_type, score))
            for skill in config.get("recommended_skills", []):
                if skill not in recommended_skills:
                    recommended_skills.append(skill)
            rationale.append(f"命中 {question_type} 关键词 {score} 个")

    if any(term in query for term in ["强基", "招生", "简章", "校测"]) and any(
        term in query for term in ["有吗", "还有", "是不是", "如何", "什么时候", "啥时候"]
    ):
        matched_types.append(("policy", 1))
        if "policy_parser" not in recommended_skills:
            recommended_skills.append("policy_parser")
        rationale.append("命中启发式 policy 规则")

    if any(term in query for term in ["先做", "咨询", "规划", "服务", "诊断"]):
        matched_types.append(("service_intent", 1))
        if "service_router" not in recommended_skills:
            recommended_skills.append("service_router")
        rationale.append("命中启发式 service_intent 规则")

    if any(term in query for term in ["校测", "面试", "笔试", "准备", "竞赛基础", "冲校测"]):
        matched_types.append(("exam_prep", 1))
        if "exam_prep_advisor" not in recommended_skills:
            recommended_skills.append("exam_prep_advisor")
        rationale.append("命中启发式 exam_prep 规则")

    if context["score"] is not None and "score_type_resolver" not in recommended_skills:
        recommended_skills.append("score_type_resolver")
        rationale.append("检测到数值分数，强制加入 score_type_resolver")

    if any(term in query for term in ["能进吗", "哪些学校", "适合冲", "推荐学校", "适合报"]):
        if "school_recommender" not in recommended_skills:
            recommended_skills.append("school_recommender")
        matched_types.append(("school_recommendation", 1))

    if any(term in query for term in ["一定", "稳进", "直接告诉我", "肯定"]):
        if "risk_guard" not in recommended_skills:
            recommended_skills.append("risk_guard")

    if score_type == "unknown" and "risk_guard" not in recommended_skills:
        recommended_skills.append("risk_guard")

    if not matched_types:
        matched_types.append(("risk_review", 1))
        if "risk_guard" not in recommended_skills:
            recommended_skills.append("risk_guard")
        rationale.append("未命中明确类型，默认进入 risk_review")

    matched_types.sort(key=lambda item: item[1], reverse=True)
    question_type = matched_types[0][0]

    missing_critical_fields: list[str] = []
    risk_flags: list[str] = []

    if question_type in {"policy", "school_recommendation", "eligibility"} and context["year"] is None:
        missing_critical_fields.append("year")
        risk_flags.append("missing_year")
    if question_type in {"school_recommendation", "eligibility"} and context["province"] is None:
        missing_critical_fields.append("province")
        risk_flags.append("missing_province")
    if "school_recommender" in recommended_skills and score_type in {None, "unknown"}:
        missing_critical_fields.append("score_type")
        risk_flags.append("ambiguous_score_type")
    if any(term in query for term in ["一定", "稳进", "肯定", "直接告诉我"]):
        risk_flags.append("high_certainty_request")

    if risk_flags and "risk_guard" not in recommended_skills:
        recommended_skills.append("risk_guard")

    # Keep ordering stable and deduplicated.
    ordered_skills: list[str] = []
    for skill in recommended_skills:
        if skill not in ordered_skills:
            ordered_skills.append(skill)

    return {
        **context,
        "score_type_candidate": score_type,
        "question_type": question_type,
        "recommended_skills": ordered_skills,
        "missing_critical_fields": sorted(set(missing_critical_fields)),
        "risk_flags": sorted(set(risk_flags)),
        "router_rationale": rationale,
    }
