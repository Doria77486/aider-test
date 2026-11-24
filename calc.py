"""Basic arithmetic and exponentiation.

Kept deliberately simple so that aider's edit behavior is easy to observe.
"""


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    # TODO: b == 0 is not handled
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
