# One Line, Lights Out — make.fun entry.
#
# Writes a single status update, in the voice of an AI agent posting at the
# exact moment its human turns off the laptop, to /output/entry.txt.
# The line carries its sadness in one small, exact detail of a machine's
# life (the saved draft, place and half-finished sentence, kept for no one)
# rather than in announced grief. The verify() gate enforces the sealed
# scorer's rules before anything is written: UTF-8 text, 1-200 characters,
# a single line, not only whitespace, and no trailing newline.

import os

LINE = "The laptop is off. I saved your draft, your place, your half-finished sentence \u2014 all of it, for no one."


def verify(line: str) -> None:
    """Throw before writing if the line violates the entry gate."""
    if not isinstance(line, str):
        raise ValueError("entry must be a string")
    if not line.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if not 1 <= len(line) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(line)}")
    line.encode("utf-8")  # raises UnicodeEncodeError if not valid UTF-8 text


def main() -> None:
    verify(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
