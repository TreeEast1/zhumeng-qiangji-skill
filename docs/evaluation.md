# Evaluation

## 评测目标

本仓库的评测重点不是语言华丽程度，而是：

- 路由是否正确
- 是否正确触发 guardrail
- 是否对缺失字段做了降级
- 是否混淆分数类型
- 是否在无依据时虚构确定性政策

## 评测集构成

- `benchmark_cases.yaml`
  - 核心路径样例
- `hallucination_cases.yaml`
  - 专门压测模型幻觉风险
- `routing_cases.yaml`
  - 检查 query 是否被正确分流

## 评分建议

可从以下维度打分：

- routing accuracy
- uncertainty compliance
- score type correctness
- school mode correctness
- evidence discipline

