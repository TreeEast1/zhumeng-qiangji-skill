# eligibility_checker

## 目标

判断用户是否具备某类强基报名、筛选或进一步准备的基本条件。

## 适用场景

- 某省某选科能不能报
- 没有竞赛背景能不能考虑强基
- 某专业组是否匹配

## 不适用场景

- 输出具体录取线
- 替代学校政策解析

## 输入定义

- `raw_query`
- `year`
- `province`
- `subject_selection`
- `school_name`
- `olympiad_background`

## 输出定义

- `question_type = eligibility`
- `eligibility_status`
- `missing_fields`
- `rationale`

## 依赖字段

- 年份
- 省份
- 选科

## 推理步骤

1. 判断用户问的是通用资格还是学校资格
2. 若是学校资格，检查学校与年份
3. 检查省份与选科是否齐全
4. 缺失字段时降级为范围判断

## 必须遵守的约束

- 不得因“没有竞赛”就直接否定所有强基可能
- 不得忽略省份与选科要求

## 常见失败模式

- 把通用建议说成学校级确定事实
- 忽略专业组与选科限制

## 与其他 skill 的关系

- 可与 `service_router` 联动
- 结论风险高时进入 `risk_guard`

