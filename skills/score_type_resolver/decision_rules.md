# score_type_resolver Decision Rules

1. 只要 query 有数字且含义不清，优先进入本 skill。
2. 出现“综合成绩”时，禁止输出 `gaokao_raw_score`。
3. 出现“入围线 / 录取线”时，要继续判断是在问历史结果、当前预估还是目标线。
4. 若不能唯一归类，输出 `unknown` 并提示澄清。

