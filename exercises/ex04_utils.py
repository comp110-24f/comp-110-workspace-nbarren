"""EX04 - List Utility Functions."""

__author__ = "730744691"


def all(int_list: list[int], num: int) -> bool:
    """Function to determine if all ints in list are equal to num."""
    idx: int = 0  # variable will be used to evaluate each number in list
    if len(int_list) == 0:  # list cannot be empty
        return False
    while idx < len(int_list):
        if int_list[idx] != num:
            return False  # function will be exited and return False if any item in list is not equal to the num
        idx += 1
    return True  # will only reach this point if all items in list are equal to the num


def max(int_list: list[int]) -> int:
    """Funtion to determine max value in list."""
    if len(int_list) == 0:  # cannot be an empty list
        raise ValueError("max() arg is an empty list")
    idx: int = 1  # idx 0 will be original max, start by evaluating it with idx 1
    max: int = int_list[
        0
    ]  # max starts with idx 0 and is then compared and changed with every other idx
    while idx < len(int_list):
        if int_list[idx] > max:
            max = int_list[idx]
        idx += 1
    return max


def is_equal(int_list1: list[int], int_list2: list[int]) -> bool:
    """Function to determine if two lists are equal to each other."""
    if len(int_list1) != len(int_list2):  # lists must be same length to be equal
        return False
    idx: int = 0
    while idx < len(int_list1) and idx < len(int_list2):
        if (
            int_list1[idx] != int_list2[idx]
        ):  # will determine if there is any index at which the two lists are not equal to each other
            return (
                False  # exits the function and returns False since lists are not equal
            )
        idx += 1
    return True  # will only reach this return statement if all indexs are equal to each other


def extend(int_list1: list[int], int_list2: list[int]) -> None:
    """Funtion to add one list to the end of another."""
    idx: int = 0
    while idx < len(int_list2):  # will go thru each idx of list2
        int_list1.append(int_list2[idx])  # adds each item in list2 to list1
        idx += 1
