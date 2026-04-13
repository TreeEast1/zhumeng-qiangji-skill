# Routing Strategy

## 一级路由维度

强基计划场景中的一级问题类型分为：

- `policy`
- `school_mode`
- `score_disambiguation`
- `eligibility`
- `school_recommendation`
- `exam_prep`
- `service_intent`
- `risk_review`

## 路由优先级

### 1. 风险前置

如果问题缺少明显关键字段，但用户要求确定性结论，先路由 `risk_guard`。

### 2. 分数歧义优先

只要用户输入出现数字分数，且未明确说明其类型，就优先经过 `score_type_resolver`。

### 3. 模式问题与政策问题联动

如果问题涉及“清北模式 / 复交南模式 / 出分前 / 出分后 / 面试 / 笔试”，优先路由 `school_mode_classifier`，必要时联动 `policy_parser`。

### 4. 择校建议强制检查省份与年份

当问题涉及“适合冲哪些学校”“能不能进某校”等，若缺少年份或省份，路由必须自动降级，并附加缺失字段提示。

## 多 skill 路由

系统默认允许一个 query 对应多个 skill。

例如：

- “江苏，2026，某校 680 能进吗”
  - `score_type_resolver`
  - `school_recommender`
  - `risk_guard`

