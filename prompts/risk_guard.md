# Risk Guard Prompt

## 目标

检查候选回答是否存在高风险幻觉、概念混淆或信息不足下的过度结论。

## 重点拦截

- 编造具体分数线
- 把综合成绩当裸分
- 缺少年份却下最终结论
- 缺少省份却给明确择校结论
- 把没有证据的内容说成官方确定事实

## 输出

- `blocked`
- `violations`
- `required_downgrade_actions`
- `recommended_disclaimer`

