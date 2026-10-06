"""
Practice Project: Failed Login Counter

Read an SSH log and print the source IPs with the most failed password
attempts, highest first.

    python3 failed_logins.py auth.log

Rules:
- Take the log path from sys.argv; print usage and exit if it's missing.
- Count only "Failed password" lines. Invalid user / Accepted /
  Connection closed lines also mention IPs but don't count.
- The IP isn't at a fixed word position ("for root from X" vs
  "for invalid user NAME from X").

Expected output for auth.log:

203.0.113.7 5
198.51.100.23 3
192.0.2.44 2
203.0.113.99 1

Hints: str.split(), list.index(), dict.get(key, 0), sorted(..., key=...).
Lines end in "\\n".
"""

import sys


def count_failures(path):
    """Return {ip: failed_attempt_count}."""
    counts = {}
    with open(path) as f:
        for line in f:
            # TODO
            pass
    return counts


def main():
    if len(sys.argv) != 2:
        print(f"usage: {sys.argv[0]} <logfile>")
        sys.exit(1)

    counts = count_failures(sys.argv[1])

    # TODO: sort and print


main()
