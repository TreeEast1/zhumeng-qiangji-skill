# Skill Index

| Skill | Primary Role | Depends On | Hands Off To |
| --- | --- | --- | --- |
| `policy_parser` | 解析政策型问题 | year, school_name, province | `risk_guard` |
| `school_mode_classifier` | 识别模式与比较模式差异 | school_name, year | `policy_parser`, `risk_guard` |
| `score_type_resolver` | 识别数字含义 | score text, context terms | `school_recommender`, `risk_guard` |
| `eligibility_checker` | 判断是否具备基本报考条件 | year, province, subject_selection | `risk_guard`, `service_router` |
| `school_recommender` | 输出保守择校建议 | year, province, score context | `score_type_resolver`, `risk_guard` |
| `exam_prep_advisor` | 输出准备路径与投入建议 | target school, baseline, olympiad background | `service_router` |
| `service_router` | 把问答转为服务动作 | consultation stage, urgency, clarity | downstream service workflow |
| `risk_guard` | 拦截高风险结论 | candidate answer, query context | final answer composer |

所有 skill 都应：

- 优先结构化字段
- 显式处理缺失字段
- 输出 evidence_status 与 risk_level
- 在高风险场景下优先保守

