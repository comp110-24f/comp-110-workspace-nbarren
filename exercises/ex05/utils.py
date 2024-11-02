"""Implementing more list utility functions."""

__author__ = "730744691"


def only_evens(input: list[int]) -> list[int]:
    """Function to return a list of even nums."""
    even_list: list[int] = (
        []
    )  # create an empty list to add values (does not mutate original list)
    idx: int = 0
    while idx < len(input):
        if (
            input[idx] % 2 == 0
        ):  # will only be true if number is even (can be divided by two with no remainder)
            even_list.append(input[idx])
        idx += 1
    return even_list


def sub(input: list[int], start: int, end: int) -> list[int]:
    """Function to obtain a subset of a list."""
    new_list: list[int] = (
        []
    )  # create empty list to add subset to (does not mutate original list)
    if (
        start < 0
    ):  # resets start value as beginning of list if index is out of range (negative)
        start = 0
    if end > len(
        input
    ):  # resets end value to end of list if index if out of range (larger than list)
        end = len(input)
    for idx in range(
        start, end
    ):  # end value is not included (which is why you do not -1 to obtain end index value)
        new_list.append(input[idx])  # adds each num in range to subset list
    return new_list


def add_at_index(input: list[int], elem: int, index: int) -> None:
    """Function to add an item to a list at a specific index."""
    if index < 0 or index > len(input):  # elem must be inserted at a viable index
        raise IndexError("Index is out of bounds for the input list")
    input.append(0)  # add index to end of list to make room for new value
    idx: int = len(input) - 1  # set up to move nums to right
    while (
        idx >= index
    ):  # loop through to move all values to the right that are right of idx where num is being inserted
        input[idx] = input[idx - 1]
        idx -= 1  # must loop through backwards to ensure all index values are accounted for before they are changed
    input[index] = elem


a: list[int] = [1, 2, 4, 5, 6]
add_at_index(a, 3, 2)
print(a)
