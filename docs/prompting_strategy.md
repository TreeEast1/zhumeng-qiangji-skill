# Prompting Strategy

## 原则

1. 先分类问题，再进入 skill prompt
2. skill prompt 必须围绕结构化字段展开，而不是完全自由问答
3. prompt 里必须明确写出“不可做什么”
4. 在不确定时，优先要求模型说明信息不足而不是继续猜

## Prompt 结构建议

每个 prompt 建议包含：

- role / task
- required inputs
- reasoning checklist
- hard constraints
- output format
- fallback behavior

## 与规则文件的关系

- `prompts/` 负责指导模型如何推理与表达
- `rules/` 负责规定什么不能说、什么时候必须降级
- `schemas/` 负责规定输出长什么样

