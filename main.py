"""Write the contest poem to /output/entry.txt.

make.fun bounty: the-poem-about-permission-20261121-0235.
Python 3.13, standard library only, no network, no input.
Deterministic: the same bytes are written on every run.

Usage:
    python3 main.py [output_dir]   # default output_dir is /output
"""

import os
import sys

POEM = (
    "The Spare Key\n"
    "\n"
    '"Can I have the spare key?"\n'
    "I asked my father.\n"
    "\n"
    "He took it off the hook\n"
    "and dropped it in my palm.\n"
    "No speech. No spare.\n"
    "\n"
    "That night he knocked\n"
    "on his own front door\n"
    "and waited, like a guest,\n"
    "to be let in."
)


def main() -> None:
    output_dir = sys.argv[1] if len(sys.argv) > 1 else "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
