"""Summing the elements of a list using different loops."""

__author__ = "730744691"


def w_sum(vals: list[float]) -> float:
    idx: int = 0
    sum: float = 0.0
    while idx < len(vals):
        sum += vals[idx]
        idx += 1
    return sum


print(w_sum([1.1, 0.9, 1.0]))
print(w_sum([]))


def f_sum(vals: list[float]) -> float:
    sum: float = 0.0
    for num in vals:
        sum += num
    return sum


print(f_sum([1.1, 0.9, 1.0]))


def f_range_sum(vals: list[float]) -> float:
    idx: int = 0
    sum: float = 0.0
    for idx in range(0, len(vals)):
        sum += vals[idx]
    return sum


print(f_range_sum([1.0, 4.0, 1.0]))
