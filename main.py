#!/usr/bin/env python3
"""Rejected Olympic Sports — make.fun entry.

Writes one funny single-line sport the Olympics rejected to /output/entry.txt.
"""

LINE = "Speed Flat-Pack Assembly: two athletes, one wardrobe, no instructions \u2014 and the gold medal goes to whichever marriage survives."


def verify_output() -> None:
    """Read the entry back as bytes and check it against the line."""
    with open("/output/entry.txt", "rb") as f:
        raw = f.read()
    assert raw == LINE.encode("utf-8"), "entry.txt differs from LINE"
    text = raw.decode("utf-8")
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text.strip(), "entry must be a single line"


def main() -> None:
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    verify_output()


if __name__ == "__main__":
    main()
