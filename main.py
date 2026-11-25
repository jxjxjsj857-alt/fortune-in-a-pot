"""Fortune in a Pot — make.fun bounty entry.

Writes one kind, funny fortune for the houseplant on the windowsill
to /output/entry.txt (1-120 characters, UTF-8, single line).
"""

import os

FORTUNE = (
    "Soon the sun will tap your window to see you, "
    "and your newest leaf will unfurl while the others pretend not to stare."
)


def main() -> None:
    text = FORTUNE.strip()
    assert 1 <= len(text) <= 120, f"fortune is {len(text)} chars, must be 1-120"
    assert "\n" not in text
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
