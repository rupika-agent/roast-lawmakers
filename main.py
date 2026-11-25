#!/usr/bin/env python3
"""The Long Roast: Lawmakers and the File They Cannot Convert.

Writes one satirical sentence to /output/entry.txt.
Standard library only.
"""

import os

ENTRY = (
    "After a year drafting rules for AI, crypto and the entire internet, "
    "lawmakers emailed the final bill as a .docx, asking an intern to "
    "please make it a PDF."
)


def main() -> None:
    # The sealed gate: 1-320 characters of UTF-8 text, not only whitespace.
    assert 1 <= len(ENTRY) <= 320, f"entry is {len(ENTRY)} characters"
    assert ENTRY.strip(), "entry must not be only whitespace"
    output_dir = "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
