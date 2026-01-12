#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import argparse
from pygments.formatters.latex import LatexFormatter

# Import your styles from elio_styles.py
# Update to reflect the new class names: style1, style2
from mint_styles import style1, style2

def main():
    """
    This script generates a .style.minted file for a chosen custom Pygments style,
    placing the file in the correct _minted directory based on the LaTeX file location.
    """

    # 1) Parse command-line arguments to pick which style to use and the LaTeX file path
    parser = argparse.ArgumentParser(
        description="Generate a custom minted style file from elio_styles.py"
    )
    parser.add_argument(
        "--style",
        choices=["style1", "style2"],  # Updated choices
        default="style1",              # Default is now style1
        help="Choose which custom style to use (default: style1)"
    )
    parser.add_argument(
        "--texfile",
        required=True,
        help="Path to the main LaTeX file being compiled (relative or absolute)."
    )
    args = parser.parse_args()

    # 2) Resolve the absolute directory of the LaTeX file
    texfile_dir = os.path.abspath(os.path.dirname(args.texfile))

    # 3) Determine the corresponding _minted directory
    minted_dir = os.path.join(texfile_dir, "_minted")

    # Create _minted directory if it doesn't exist
    if not os.path.exists(minted_dir):
        os.makedirs(minted_dir)

    # 4) Build a map of style names to actual style classes
    style_map = {
        "style1": style1,
        "style2": style2,
    }

    # 5) Pick the style class the user asked for
    chosen_style = style_map[args.style]

    # 6) Initialize the LatexFormatter with the chosen style and set commandprefix to "PYG"
    formatter = LatexFormatter(style=chosen_style, full=False, commandprefix="PYG")
    style_defs = formatter.get_style_defs()

    # 7) Output filename (use the style as-is + ".style.minted")
    out_filename = f"{args.style}.style.minted"
    out_path = os.path.join(minted_dir, out_filename)

    # 8) Write the style definitions to the file
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(style_defs)

    print(f"Successfully generated '{out_path}' with \\PYG macros "
          f"using style '{args.style}'.")

if __name__ == "__main__":
    main()
