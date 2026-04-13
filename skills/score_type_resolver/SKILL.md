# score_type_resolver

## 目标

识别用户提到的数字到底属于高考裸分、综合成绩、入围线、录取线、校测分、加权分还是不明确。

## 适用场景

- “680 能进吗”
- “综合成绩 780 算高吗”
- “这个学校去年的 675 是入围线还是录取线”

## 不适用场景

- 直接代替择校或录取判断
- 在分数类型不明时给出确定性的“能进 / 不能进”

## 输入定义

- `raw_query`
- `score`
- `year`
- `school_name`
- `province`

## 输出定义

- `question_type = score_disambiguation`
- `resolved_score_type`
- `confidence_band`
- `needs_clarification`

## 依赖字段

- 数字本身
- 周边上下文词，如“裸分 / 综合成绩 / 入围线 / 录取线 / 校测”

## 推理步骤

1. 找到数字与单位
2. 找到数字附近的术语线索
3. 判断是否能唯一归类
4. 不能唯一归类则明确输出 `unknown`

## 必须遵守的约束

- 禁止默认把数字当裸分
- 禁止把综合成绩映射为裸分
- 未消歧前不得给录取判断

## 常见失败模式

- 看见 680 就当作高考裸分
- 把学校公布的综合成绩当录取裸分门槛

## 与其他 skill 的关系

- 常作为 `school_recommender` 前置 skill
- 高风险数字结论需交给 `risk_guard`

