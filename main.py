"""CLI entry point for aider-test.

Usage:
    python3 main.py add 1 2
    python3 main.py div 10 4
"""

import sys

from calc import OPERATIONS
from utils import format_result, parse_number, warn


def run(argv):
    if len(argv) != 4:
        warn("usage: main.py <op> <a> <b>")
        return 1

    _, op, a_text, b_text = argv

    if op not in OPERATIONS:
        warn(f"unknown operation: {op}")
        warn(f"available operations: {', '.join(sorted(OPERATIONS))}")
        return 1

    try:
        a = parse_number(a_text)
        b = parse_number(b_text)
    except ValueError:
        warn("arguments must be numbers")
        return 1

    result = OPERATIONS[op](a, b)
    print(format_result(result))
    return 0


if __name__ == "__main__":
    sys.exit(run(sys.argv))
