# school_recommender Decision Rules

1. 缺少年份 -> 不给最终结论。
2. 缺少省份 -> 不给明确学校名单。
3. 分数类型不明 -> 先转 `score_type_resolver`。
4. 无可靠来源 -> 只能做风险分层，不给具体线差判断。

