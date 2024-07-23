import re
from typing import Callable


def generator_numbers(text: str):
    pattern = r"\b\d+\.\d+\b"
    for match in re.finditer(pattern, text):
        yield float(match.group())


def sum_profit(text: str, func: Callable):
    total = sum(
        func(text)
    )
    return total