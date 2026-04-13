# Skill System

## Skill 设计原则

每个 skill 都必须回答四个问题：

1. 它解决什么问题？
2. 它不解决什么问题？
3. 它依赖哪些输入字段？
4. 它产出的输出在系统里怎样被消费？

## Skill 编排关系

- `master_router` 决定主路由
- `risk_guard` 作为全局兜底 skill，可以在前置或后置执行
- `score_type_resolver` 是多个 skill 的前置能力，因为分数含义经常不清
- `policy_parser` 与 `school_mode_classifier` 经常组合出现
- `service_router` 不直接回答政策结论，而是把咨询任务分流到下一动作

## Skill 输出要求

所有 skill 输出都应尽量对齐 `schemas/answer.schema.json`，至少包含：

- `conclusion`
- `rationale`
- `evidence_status`
- `risk_level`
- `next_step`
- `disclaimer`

