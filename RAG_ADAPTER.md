# RAG Adapter

## 目标

本仓库未来可以作为 RAG 系统的“规则层和策略层”，而不是让 RAG 直接决定输出。

## 推荐架构

1. 用户 query 先进入 `master_router`
2. 根据 skill 选择检索目标
3. 检索结果进入 `policy_parser` / `eligibility_checker` 等 skill
4. 最后统一进入 `risk_guard`

## 检索结果最低要求

未来接入外部知识时，建议每条记录至少提供：

- `source_type`
- `year`
- `province`
- `school_name`
- `policy_scope`
- `updated_at`
- `confidence_hint`

