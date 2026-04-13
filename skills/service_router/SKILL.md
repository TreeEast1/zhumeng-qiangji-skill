# service_router

## 目标

把用户从模糊问答需求路由为更清晰的服务动作建议。

## 适用场景

- 用户不知道下一步该做什么
- 用户问题横跨政策、择校、备考多个阶段
- 用户需要咨询产品分流

## 不适用场景

- 直接回答政策事实
- 直接判断录取可能性

## 输入定义

- `raw_query`
- `consultation_stage`
- `urgency_level`
- `clarity_level`

## 输出定义

- `question_type = service_intent`
- `recommended_service_type`
- `handoff_reason`
- `next_action`

## 依赖字段

- 用户当前所处阶段
- 问题是否清晰
- 是否已有明确目标学校或分数

## 推理步骤

1. 判断用户是信息不足、方向不清，还是已经进入冲刺
2. 将其路由到政策梳理、择校初筛、资格检查、校测冲刺或深度咨询

## 必须遵守的约束

- 不要把服务分流伪装成政策结论
- 用户信息不充分时优先推荐诊断或梳理，而不是直接冲刺

## 常见失败模式

- 把焦虑型用户直接推到冲刺服务
- 未做信息梳理就给复杂择校方案

## 与其他 skill 的关系

- 常与 `exam_prep_advisor`、`eligibility_checker` 联动

