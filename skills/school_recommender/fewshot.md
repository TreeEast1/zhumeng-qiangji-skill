# school_recommender Few-shot

## Example 1

输入：`江苏，2026，物化生，某校 680 能进吗？`

输出约束：

- 如果 680 含义不清，先要求 score disambiguation
- 不直接输出“稳进”

## Example 2

输入：`675 分适合冲哪些学校？`

输出约束：

- 若没有省份，不能列明确学校名单
- 只能提示需补充省份和年份

