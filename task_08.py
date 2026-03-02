import re
from functools import reduce
from operator import mul


def multiply_numbers(inputs=None):
    if inputs is None:
        return None

    s = str(inputs)
    digits = re.findall(r'\d', s)

    if not digits:
        return None

    return reduce(mul, (int(d) for d in digits))
