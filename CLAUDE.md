# Airis Marketplace

A Claude Code plugin marketplace maintained by Airis.

## What is a Plugin?

A Claude Code plugin is a package that extends Claude's capabilities. Plugins can include:

- **Skills**: Slash commands (`/skill-name`) that inject prompts or workflows
- **Hooks**: Automated actions triggered by events (e.g., run linting after file edits)
- **Agents**: Specialized subagents for specific tasks
- **MCP Servers**: External tool integrations
- **Commands**: Simple markdown-based user commands (legacy, prefer skills)

## Plugin Structure

```
plugin-name/
├── .claude-plugin/
│   └── plugin.json      # Required: plugin metadata
├── skills/
│   └── skill-name/
│       └── SKILL.md     # Skill definition with frontmatter
├── hooks/
│   └── hooks.json       # Or define inline in plugin.json
├── agents/
│   └── agent-name.md
└── scripts/             # Supporting scripts for hooks/skills
```

Key rule: Only `plugin.json` goes inside `.claude-plugin/`. Everything else (skills, hooks, agents) stays outside.

## Creating a New Plugin

1. Read the official docs:
   - [Create plugins](https://code.claude.com/docs/en/plugins.md) - core concepts and structure
   - [Plugins reference](https://code.claude.com/docs/en/plugins-reference.md) - full schema details
   - [Plugin marketplaces](https://code.claude.com/docs/en/plugin-marketplaces.md) - distribution

2. For skills specifically:
   - [Agent skills overview](https://code.claude.com/docs/en/agents-and-tools/agent-skills/overview.md)
   - Review existing skills in this repo under `plugins/*/skills/`

3. For hooks:
   - [Hooks documentation](https://code.claude.com/docs/en/hooks.md)
   - See `plugins/ruff-hooks/` for a working example

4. For prompts in skills:
   - [Claude prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-4-best-practices.md)

## Adding a Plugin to This Marketplace

1. Create your plugin under `plugins/your-plugin-name/`
2. Add an entry to `.claude-plugin/marketplace.json`
3. Update the README table
4. Submit a PR
