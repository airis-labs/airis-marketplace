---
description: Render combined slides to HTML
argument-hint: [path]
allowed-tools: Bash(marp:*)
---

Render slides in: ${1:-.}

!`cd "${1:-.}" && marp combined_slides.md -o slides.html`

Report the result and remind to open slides.html to review.
