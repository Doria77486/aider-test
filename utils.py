"""输入解析与输出格式化。

留了几个小坑，方便测试模型是否能正确修改。
"""

import json  # 未使用，方便触发 lint
import sys


def parse_number(text):
    """把字符串转成数字。

    已知问题：不支持负数。
    """
    if text.isdigit():
        return int(text)
    return float(text)


def format_result(value):
    """把结果格式化成字符串，整数不带小数点。"""
    if isinstance(value, float) and value.is_integer():
        return str(int(value))
    return str(value)


def dump_json(data):
    return json.dumps(data, ensure_ascii=False)


def warn(msg):
    print(f"warning: {msg}", file=sys.stderr)
