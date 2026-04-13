# GPT Adapter

## 用途

本文件说明如何将本仓库迁移到 ChatGPT 自定义 GPT 或类似 agent 配置中。

## 建议映射

- `prompts/system_prompt.md`
  - 作为系统提示主干
- `prompts/master_router.md`
  - 作为内部路由说明
- `rules/*.yaml`
  - 转写为不可违反的显式约束
- `knowledge/glossary/terminology.md`
  - 作为术语附录
- `examples/` + `evals/`
  - 作为调试和回归集

## 建议保留的强约束

- 缺少年份或省份时禁止直接给最终结论
- 分数类型不明时必须先澄清或降级
- 对高风险输出附加 disclaimer

