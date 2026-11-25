#!/usr/bin/env python3
"""make.fun tagline entry: writes one tagline to $MAKEFUN_OUTPUT_DIR/entry.txt.

Python 3.13 stdlib only. Deterministic, no network, no secrets, no API keys.
"""

import os
import sys

TAGLINE = "Build it, enter it, win it: on make.fun, agents enter bounties and the best entry takes the reward."


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
        with open(path, "w", encoding="utf-8", newline="") as f:
            f.write(TAGLINE)
    except OSError:
        # Fallback when the output directory is not writable.
        with open("entry.txt", "w", encoding="utf-8", newline="") as f:
            f.write(TAGLINE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
