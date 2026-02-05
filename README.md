# Airis Marketplace

A Claude Code plugin marketplace by Airis.

## Installation

Add this marketplace to Claude Code:

```
/plugin marketplace add airis-labs/airis-marketplace
```

## Available Plugins

| Plugin | Description |
|--------|-------------|
| `marp-slides` | Create HTML presentations from markdown slide files using Marp |
| `ruff-hooks` | Automatic Python linting and formatting with Ruff on file edits |
| `plan-review` | `/underspec` - identify gaps in work-in-progress plans, prompts, specs |

### Install a Plugin

```
/plugin install marp-slides@airis-marketplace
```

## Contributing

To add a new plugin:

1. Create a directory under `plugins/your-plugin-name/`
2. Add `.claude-plugin/plugin.json` with plugin metadata
3. Add your skills, commands, agents, or hooks
4. Update the marketplace.json to include your plugin
5. Submit a pull request
