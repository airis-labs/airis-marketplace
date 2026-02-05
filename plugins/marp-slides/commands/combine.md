---
description: Combine slide markdown files into a single Marp deck
argument-hint: [path]
allowed-tools: Bash(python:*)
---

Combine slides in: ${1:-.}

!`python ${CLAUDE_PLUGIN_ROOT}/skills/marp-slides/scripts/combine.py "${1:-.}" --style ${CLAUDE_PLUGIN_ROOT}/assets/style.yaml`

Report the result.
