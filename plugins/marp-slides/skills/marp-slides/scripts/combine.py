#!/usr/bin/env python3
"""
Combine individual slide markdown files into a single Marp presentation.

Usage: python combine.py <slide_directory> [--style <path_to_default_style.yaml>]

Reads style.yaml from slide_directory for frontmatter.
If style.yaml is missing, copies from the provided default style path.
Outputs combined_slides.md in the slide directory.
"""

import argparse
import shutil
import sys
from pathlib import Path


def combine_slides(slide_dir: Path, default_style_path: Path | None = None) -> None:
    """Combine all .md files in slide_dir into combined_slides.md."""

    # Files to ignore (meta documentation, not slides)
    IGNORE_FILES = {
        "combined_slides.md",
        "CLAUDE.md",
        "README.md",
    }

    # Find all markdown files (excluding ignored files)
    slide_files = sorted(f for f in slide_dir.glob("*.md") if f.name not in IGNORE_FILES)

    if not slide_files:
        print(f"No markdown files found in {slide_dir}")
        sys.exit(1)

    # Load style from style.yaml or copy default
    style_file = slide_dir / "style.yaml"
    if style_file.exists():
        style_content = style_file.read_text().strip()
    elif default_style_path and default_style_path.exists():
        shutil.copy(default_style_path, style_file)
        style_content = style_file.read_text().strip()
        print(f"Created {style_file} from default template")
    else:
        print(f"Error: No style.yaml found in {slide_dir} and no default provided")
        sys.exit(1)

    # Build combined output
    output = f"---\n{style_content}\n---\n\n"

    for i, slide_file in enumerate(slide_files):
        content = slide_file.read_text().strip()

        # Add fit class for slides with dense content
        if content.count("```") >= 2 or content.count("|") >= 8:
            output += "<!-- _class: fit -->\n"

        output += content

        # Add separator between slides (not after last)
        if i < len(slide_files) - 1:
            output += "\n\n---\n\n"
        else:
            output += "\n"

    # Write combined output
    output_file = slide_dir / "combined_slides.md"
    output_file.write_text(output)

    print(f"Combined {len(slide_files)} slides into {output_file}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Combine slide markdown files")
    parser.add_argument("slide_directory", type=Path, help="Directory containing slide .md files")
    parser.add_argument("--style", type=Path, help="Path to default style.yaml template")
    args = parser.parse_args()

    if not args.slide_directory.is_dir():
        print(f"Error: {args.slide_directory} is not a directory")
        sys.exit(1)

    combine_slides(args.slide_directory, args.style)
