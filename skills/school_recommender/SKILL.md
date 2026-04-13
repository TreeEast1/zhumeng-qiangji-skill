# school_recommender

## 目标

在信息充分前提下给出保守、分层的学校建议；在信息不足时明确降级。

## 适用场景

- 这个分数适合冲哪些学校
- 某校是否值得重点关注
- 哪些学校风险较高

## 不适用场景

- 分数类型不明
- 缺少年份或省份却要求最终学校名单

## 输入定义

- `raw_query`
- `year`
- `province`
- `score`
- `rank`
- `subject_selection`
- `school_name`

## 输出定义

- `question_type = school_recommendation`
- `recommendation_band`
- `candidate_schools`
- `rationale`

## 依赖字段

- 年份
- 省份
- 分数或位次
- 分数类型

## 推理步骤

1. 先确认问题是否真的在问推荐
2. 检查年份和省份是否齐全
3. 检查分数类型是否明确
4. 若信息不足，降级为“可关注范围”而不是学校名单

## 必须遵守的约束

- 不得在无省份时输出明确学校名单
- 不得在无年份时输出最终判断
- 建议分级只能使用：可尝试 / 可重点关注 / 不能确认 / 风险较高

## 常见失败模式

- 用一个模糊分数直接列学校
- 忽略位次与省份差异

## 与其他 skill 的关系

- 强依赖 `score_type_resolver`
- 强绑定 `risk_guard`

