---
description: Combine and render slides to HTML (full build)
argument-hint: [path]
allowed-tools: Bash(python:*, marp:*)
---

Build slides in: ${1:-.}

Step 1 - Combine:
!`python ${CLAUDE_PLUGIN_ROOT}/skills/marp-slides/scripts/combine.py "${1:-.}" --style ${CLAUDE_PLUGIN_ROOT}/assets/style.yaml`

Step 2 - Render:
!`cd "${1:-.}" && marp combined_slides.md -o slides.html`

Report the result and remind to open slides.html to review.
