"""Input parsing and output formatting.

A few rough edges are left in place so that model edits are easy to verify.
"""

import json  # unused, kept to trigger lint
import sys


def parse_number(text):
    """Convert a string to a number.

    Known issue: negative numbers are not supported.
    """
    if text.isdigit():
        return int(text)
    return float(text)


def format_result(value):
    """Format a result as a string, without a trailing .0 for integers."""
    if isinstance(value, float) and value.is_integer():
        return str(int(value))
    return str(value)


def dump_json(data):
    return json.dumps(data, ensure_ascii=False)


def warn(msg):
    print(f"warning: {msg}", file=sys.stderr)
