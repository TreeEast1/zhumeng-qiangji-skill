# score_type_resolver Few-shot

## Example 1

输入：`某校 680 能进吗？`

输出约束：

- resolved_score_type 不能直接等于 `gaokao_raw_score`
- needs_clarification = true

## Example 2

输入：`这个学校去年综合成绩 780 是什么概念？`

输出约束：

- resolved_score_type = `composite_score`
- 不能把它说成裸分

