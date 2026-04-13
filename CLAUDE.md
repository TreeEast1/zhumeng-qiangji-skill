# Claude Skill Usage Note

本仓库可直接迁移为 Claude Skills 风格的能力底座：

- `skills/*/SKILL.md` 可直接作为 skill description 的基础素材
- `prompts/system_prompt.md` 可作为系统级约束
- `rules/` 可转写为调用前检查与后处理逻辑
- `schemas/` 可作为 structured output contract

建议迁移方式：

1. 将 `master_router.md` 作为总路由器
2. 将每个 `skills/<name>/SKILL.md` 拆成独立 skill
3. 保持 `risk_guard` 为全局兜底 skill

