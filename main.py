"""Last Text at One Percent — make.fun entry.

Writes one final text message from a dying phone at 1% battery
to /output/entry.txt.
Deterministic: the same line, byte for byte, on every run.
No network, no secrets, no input read.
"""

import os

TEXT = (
    # Three beats, in the phone's own voice: what it kept (specific
    # inventory), what it forgives (the drops, the toilet, the 3 a.m.
    # doomscrolls), and the twist — it would rather go out cool
    # than be rescued by the charger.
    "1%. it's me. i kept all 4,217 of your photos, yes, even the 400 "
    "blurry ones of the dog. i forgive the drops, the toilet, the 3 a.m. "
    "doomscrolls. don't tell the charger. let me go out cool."
)


def main() -> None:
    # Gate: 1-200 chars, one line, not only whitespace. No trailing
    # newline, so the file holds exactly the line the judge reads.
    assert 1 <= len(TEXT) <= 200, len(TEXT)
    assert "\n" not in TEXT and TEXT.strip()
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
