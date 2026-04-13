# Contributing

欢迎为 `zhumeng-qiangji-skill` 贡献规则、schema、eval case 和 skill 设计，但请遵守以下约束：

## 贡献原则

1. 不要把未经核验的信息写成确定事实。
2. 新增任何政策相关字段时，优先绑定 `year` 与 `province`。
3. 新增数字类结论时，必须同时说明该数字的分数类型。
4. 新增 few-shot、benchmark、mock data 时，明确标注其用途与边界。
5. 优先修改结构化文件，再补充说明文档，不要只加自由文本 prompt。

## 推荐工作流

1. 更新 `rules/` 或 `schemas/`
2. 同步更新相关 `skills/*/SKILL.md`
3. 补充 `examples/` 与 `evals/`
4. 运行：

```bash
python scripts/validate_schemas.py
pytest
```

## Pull Request 建议

- PR 标题建议使用：`feat: ...`、`docs: ...`、`rules: ...`、`evals: ...`
- 若涉及真实政策映射，请在 PR 描述里写清楚：
  - 数据来源类型
  - 是否有年份限制
  - 是否有省份限制
  - 是否会影响现有 guardrails

