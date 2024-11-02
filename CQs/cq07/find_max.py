__author__ = "730744691"


def find_and_remove_max(input: list[int]) -> int:
    """Finds, removes, and returns largest num in a list."""
    if len(input) == 0:
        return -1
    max: int = int()
    for num in input:
        if num > max:
            max = num
    idx: int = 0
    while idx < len(input):
        if input[idx] == max:
            input.pop(idx)
        idx += 1
    return max


a: list[int] = [1, 8, 2, 3, 3]
find_and_remove_max(a)
print(a)
