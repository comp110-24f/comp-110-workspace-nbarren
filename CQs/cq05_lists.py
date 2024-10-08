"""Mutating functions."""

__author__ = "730744691"

list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1


def manual_append(list: list[int], append: int) -> None:
    list.append(append)


# a: list[int] = [1, 2, 3]
# manual_append(a, 2)
# print(a)


def double(list: list[int]) -> None:
    idx: int = 0
    while idx < len(list):
        list[idx] = list[idx] * 2
        idx += 1


# double(a)
# print(a)

double(list_2)
print(list_1)
print(list_2)
