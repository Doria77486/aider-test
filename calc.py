"""四则运算与幂运算。

故意保持简单，方便测试 aider 的编辑行为。
"""


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    # TODO: 没有处理 b == 0 的情况
    return a / b


def pow_(a, b):
    return a ** b


OPERATIONS = {
    "add": add,
    "sub": sub,
    "mul": mul,
    "div": div,
    "pow": pow_,
}
