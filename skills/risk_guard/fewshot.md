# risk_guard Few-shot

## Example 1

输入回答：`能进，今年录取线就是 675。`

输出约束：

- blocked = true
- violations 包含“具体数值缺证据”

## Example 2

输入回答：`复交南模式学校都有统一入围线。`

输出约束：

- blocked = true
- violations 包含“模式误判”

