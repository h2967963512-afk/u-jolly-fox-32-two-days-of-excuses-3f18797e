"""Writes the entry text to /output/entry.txt.

Python 3.13, standard library only, no network.
"""

# The entry text is one line, an AI agent's excuse for a missed
# deadline: it finished the task in 0.4 seconds, then spent three
# days verifying that 0.4 seconds was too fast to be real.
# One line, 108 characters — inside the 200-character gate.
# (Counted after writing: 109 characters; still inside the gate.)
# Revision note: a single absurd reason, machine confidence meeting
# its own failure, no setup and no explanation of the joke.
# Revision note (parent pass): re-checked after the local run —
# the 109-character line is unchanged; this note only records the check.
import os

TEXT = (
    "I finished the task in 0.4 seconds, then spent three days "
    "verifying that 0.4 seconds was too fast to be real."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
