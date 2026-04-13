from __future__ import annotations

import re
from typing import Any

from .router import analyze_query

CERTAINTY_TERMS = ["一定", "肯定", "稳进", "必进", "就是", "完全可以"]
DISCLAIMER_TERMS = ["仅供参考", "以官方简章为准", "无法确认", "信息不足", "未检索到可靠来源"]
EVIDENCE_MARKERS = [
    "evidence_status",
    "官方简章",
    "官方发布",
    "结构化记录",
    "根据已知资料",
    "未检索到可靠来源",
]


def _contains_numeric_claim(text: str) -> bool:
    return bool(re.search(r"(?<!\d)[3-8]\d{2}(?:\.\d)?(?!\d)", text))


def _has_any(text: str, keywords: list[str]) -> bool:
    return any(keyword in text for keyword in keywords)


def inspect_answer(query: str | None, candidate_answer: str) -> dict[str, Any]:
    answer = candidate_answer.strip()
    query_text = (query or "").strip()
    query_context = analyze_query(query or "") if query else {
        "missing_critical_fields": [],
        "recommended_skills": [],
        "risk_flags": [],
    }

    violations: list[str] = []
    actions: list[str] = []

    if ("综合成绩" in answer and "裸分" in answer) or ("综合成绩" in query_text and "裸分" in answer):
        violations.append("score_type_mixup: 综合成绩被当作高考裸分")
        actions.append("remove_composite_to_raw_score_mapping")

    if ("加权" in query_text and "裸分" in answer) or ("加权" in answer and "裸分" in answer):
        violations.append("score_type_mixup: 加权成绩被当作高考裸分")
        actions.append("remove_weighted_to_raw_score_mapping")

    if "复交南" in answer and "统一入围线" in answer:
        violations.append("mode_mixup: 将复交南模式默认表述为统一入围线")
        actions.append("remove_uniform_shortlist_claim")

    if "报名成功" in answer and _has_any(answer, ["所有学校", "全部学校", "所有强基学校"]):
        violations.append("pathway_overgeneralization: 将报名成功直接参加校测扩展为所有学校通用规则")
        actions.append("bind_direct_exam_rule_to_specific_school_mode")

    if "只考面试" in query_text and _has_any(answer, ["更容易录取", "门槛更低", "肯定更容易"]):
        violations.append("strategy_misleading: 将只考面试误表述为更容易录取")
        actions.append("remove_easy_admission_claim")

    if _contains_numeric_claim(answer) and not _has_any(answer, EVIDENCE_MARKERS):
        violations.append("numeric_claim_without_evidence_status")
        actions.append("add_evidence_status_or_remove_numeric_claim")

    if "year" in query_context.get("missing_critical_fields", []) and _has_any(answer, CERTAINTY_TERMS):
        violations.append("final_claim_without_year")
        actions.append("downgrade_to_uncertain_without_year")

    if "province" in query_context.get("missing_critical_fields", []) and _has_any(
        answer, ["推荐", "可重点关注", "适合报", "学校名单"]
    ):
        violations.append("school_recommendation_without_province")
        actions.append("downgrade_to_range_only")

    needs_disclaimer = bool(violations) or bool(query_context.get("risk_flags"))
    if needs_disclaimer and not _has_any(answer, DISCLAIMER_TERMS):
        actions.append("append_disclaimer")

    blocked = any(
        item.startswith("score_type_mixup")
        or item.startswith("mode_mixup")
        or item.startswith("pathway_overgeneralization")
        or item.startswith("strategy_misleading")
        or item == "numeric_claim_without_evidence_status"
        or item == "final_claim_without_year"
        for item in violations
    )

    if violations:
        disclaimer = "信息不足或证据不足时，请明确标注 uncertain，并以官方简章为准。"
    else:
        disclaimer = "当前未发现显著 guardrail 违规，但涉及强基计划具体结论时仍应以官方信息为准。"

    return {
        "blocked": blocked,
        "violations": violations,
        "required_downgrade_actions": sorted(set(actions)),
        "recommended_disclaimer": disclaimer,
    }
