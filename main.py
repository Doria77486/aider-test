"""aider-test 的 CLI 入口。

用法：
    python3 main.py add 1 2
    python3 main.py div 10 4
"""

import sys

from calc import OPERATIONS
from utils import format_result, parse_number, warn


def run(argv):
    if len(argv) != 4:
        warn("用法: main.py <op> <a> <b>")
        return 1

    _, op, a_text, b_text = argv

    if op not in OPERATIONS:
        warn(f"未知操作: {op}")
        warn(f"可用操作: {', '.join(sorted(OPERATIONS))}")
        return 1

    try:
        a = parse_number(a_text)
        b = parse_number(b_text)
    except ValueError:
        warn("参数必须是数字")
        return 1

    result = OPERATIONS[op](a, b)
    print(format_result(result))
    return 0


if __name__ == "__main__":
    sys.exit(run(sys.argv))
