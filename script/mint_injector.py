#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import argparse
from pygments.formatters.latex import LatexFormatter
from pygments.style import Style
from pygments.styles import get_all_styles

import mint_styles

def collect_custom_styles():
    style_map = {}
    for obj in vars(mint_styles).values():
        if isinstance(obj, type) and issubclass(obj, Style) and obj is not Style:
            name = getattr(obj, "name", None) or obj.__name__
            if name:
                style_map[name] = obj
    return style_map

def resolve_source_paths():
    sources = [mint_styles.__file__, __file__]
    resolved = []
    for path in sources:
        if not path:
            continue
        if path.endswith(".pyc") and os.path.exists(path[:-1]):
            path = path[:-1]
        resolved.append(os.path.abspath(path))
    return resolved

def is_up_to_date(out_path, sources):
    if not os.path.exists(out_path):
        return False
    out_mtime = os.path.getmtime(out_path)
    for src in sources:
        if os.path.exists(src) and os.path.getmtime(src) > out_mtime:
            return False
    return True

def main():
    """
    This script generates a .style.minted file for a chosen custom Pygments style
    found in mint_styles.py, placing the file in the correct _minted directory
    based on the LaTeX file location.
    """

    # Parse command-line arguments to pick which style to use and the LaTeX file path
    parser = argparse.ArgumentParser(
        description="Generate a custom minted style file from mint_styles.py"
    )
    parser.add_argument(
        "--style",
        default="style1",
        help="Style name to use (default: style1)"
    )
    parser.add_argument(
        "--texfile",
        required=True,
        help="Path to the main LaTeX file being compiled (relative or absolute)."
    )
    args = parser.parse_args()

    # Resolve the absolute directory of the LaTeX file
    texfile_dir = os.path.abspath(os.path.dirname(args.texfile))

    # Determine the corresponding _minted directory
    minted_dir = os.path.join(texfile_dir, "_minted")

    # Create _minted directory if it doesn't exist
    if not os.path.exists(minted_dir):
        os.makedirs(minted_dir)

    # Build a map of style names to style classes from mint_styles.py
    style_map = collect_custom_styles()
    style_name = args.style

    # Skip if the style is not a custom style defined in mint_styles.py
    if style_name not in style_map:
        if style_name in set(get_all_styles()):
            print(f"Style '{style_name}' is built-in; no custom file generated.")
            return 0
        print(f"Style '{style_name}' not found in mint_styles.py; no custom file generated.")
        return 0

    # Pick the style class the user asked for
    chosen_style = style_map[style_name]

    # Initialize the LatexFormatter with the chosen style and set commandprefix to "PYG"
    formatter = LatexFormatter(style=chosen_style, full=False, commandprefix="PYG")
    style_defs = formatter.get_style_defs()

    # Output filename (use the style as-is + ".style.minted")
    out_filename = f"{style_name}.style.minted"
    out_path = os.path.join(minted_dir, out_filename)

    # Skip regeneration if cached file is newer than sources
    sources = resolve_source_paths()
    if is_up_to_date(out_path, sources):
        print(f"'{out_path}' is up to date; skipping regeneration.")
        return 0

    # Write the style definitions to the file
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(style_defs)

    print(f"Successfully generated '{out_path}' with \\PYG macros "
          f"using style '{style_name}'.")

if __name__ == "__main__":
    main()
