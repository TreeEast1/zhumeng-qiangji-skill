# risk_guard

## 目标

对候选回答进行风险复核，拦截高风险幻觉、分数类型混淆、缺失字段下的过度结论。

## 适用场景

- 缺少年份却给最终结论
- 缺少省份却给学校名单
- 输出具体分数线但没有证据
- 把综合成绩当裸分
- 把复交南模式默认说成统一入围线

## 不适用场景

- 代替所有内容生成
- 代替路由

## 输入定义

- `raw_query`
- `candidate_answer`
- `question_type`
- `detected_missing_fields`

## 输出定义

- `blocked`
- `violations`
- `required_downgrade_actions`
- `recommended_disclaimer`

## 依赖字段

- 用户问题上下文
- 候选回答文本
- 已知缺失字段

## 推理步骤

1. 检查是否存在高风险确定性语言
2. 检查是否存在分数类型混淆
3. 检查是否存在模式混淆
4. 检查是否缺乏年份/省份/证据状态

## 必须遵守的约束

- 信息不足时必须降级
- 无可靠来源时必须显式标记 uncertain 或 missing_reliable_source
- 高风险输出必须带 disclaimer

## 常见失败模式

- 没有拦住“稳进”“肯定能进”
- 没有拦住“综合成绩 = 裸分”
- 没有拦住“复交南模式统一入围线”

## 与其他 skill 的关系

- 可作为全局前置或后置 skill

