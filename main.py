# u-ronigrv-the-one-line-laugh-7ccca46f entry: one funny line about houseplants.
#
# The line is a fixed string: the program is deterministic by construction,
# so two runs write the same bytes. It reads $MAKEFUN_OUTPUT_DIR when set,
# else /output, and writes entry.txt there.

import os

LINE = "I told my ferns I was going away for the weekend, and when I got back they had started a book club and refused to let me join."

# The gate allows 1 to 200 characters; refuse to write an over-long line
# rather than submit an entry the scorer would mark invalid.
MAX_CHARS = 200

def main():
    if not 1 <= len(LINE) <= MAX_CHARS:
        raise SystemExit(f"entry is {len(LINE)} chars, outside the 1-{MAX_CHARS} gate")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
