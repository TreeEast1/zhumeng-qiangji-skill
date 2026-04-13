# policy_parser Few-shot

## Example 1

输入：`2026 年星河大学还有强基吗？`

输出约束：

- question_type = `policy`
- 若无官方证据，仅能回答“需以当年简章为准”

## Example 2

输入：`某校强基是不是出分前校测？`

输出约束：

- 若未给学校和年份，不能直接回答
- 需要提示补充 `school_name` 和 `year`

