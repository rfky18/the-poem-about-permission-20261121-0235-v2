"""Write the contest poem to /output/entry.txt.

make.fun bounty: the-poem-about-permission-20261121-0235.

The poem, "The Spare Key", is about permission as agency: a father hands
his child the spare key to the house, and that night he knocks on his own
front door and waits, like a guest, to be let in. Giving permission means
giving up control of the threshold.

Python 3.13, standard library only, no network, no input.
Deterministic: the same bytes are written on every run, because POEM is a
fixed literal and the file is written verbatim with no timestamp, no
randomness, and no trailing newline added.

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
        # Write POEM exactly as-is: no trailing newline is appended, so the
        # output stays byte-identical (219 chars) on every run.
        f.write(POEM)


if __name__ == "__main__":
    main()
