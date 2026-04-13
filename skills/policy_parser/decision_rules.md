# policy_parser Decision Rules

1. 若没有 `year`，默认不能下最终政策结论。
2. 若问题涉及“招生省份 / 选科 / 专业组”，没有 `province` 时只能部分回答。
3. 若问题包含“模式”，联动 `school_mode_classifier`。
4. 若结论将影响报考动作，输出必须附带风险提示。

