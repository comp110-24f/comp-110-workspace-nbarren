from exercises.ex05.utils import only_evens, sub, add_at_index

import pytest  # used for checking for raised IndexError

"""Defining unit tets for util functions."""

__author__ = "730744691"


def test_only_evens_return() -> None:
    """Tests that only evens returns correct int list (use case)."""
    a: list[int] = [1, 2, 3, 4, 5, 6]  # create list to test on
    assert only_evens(a) == [2, 4, 6]


def test_only_evens_mutate() -> None:
    """Tests that only_evens does not mutate list (use case)."""
    a: list[int] = [1, 2, 3, 4, 5, 6]
    only_evens(a)
    assert a == [1, 2, 3, 4, 5, 6]  # a should be original list (not evens)


def test_only_evens_inputs() -> None:
    """Tests that only_evens works with an empty list (edge case)."""
    a: list[int] = []
    assert only_evens(a) == []  # return empty list if list is empty


def test_sub_return() -> None:
    """Tests that sub returns correct subset list (use case)."""
    a: list[int] = [1, 2, 3, 4, 5, 6]
    assert sub(a, 1, 3) == [2, 3]


def test_sub_mutate() -> None:
    """tests that sub does not mutate list (use case)."""
    a: list[int] = [1, 2, 3, 4, 5, 6]
    sub(a, 1, 3)
    assert a == [1, 2, 3, 4, 5, 6]  # a should be original list (not subset)


def test_sub_input() -> None:
    """Tests that sub works when input indices are out of range (edge case)."""
    a: list[int] = [1, 2, 3, 4, 5, 6]
    assert sub(a, -4, 13) == [
        1,
        2,
        3,
        4,
        5,
        6,
    ]  # returns whole list (start value = 0 and end value = len(list)) if indices entered are out of range


def test_add_at_index_return() -> None:
    """tests that add at index returns none (use case)."""
    a: list[int] = [1, 2, 3, 4, 5, 6]
    assert (
        add_at_index(a, 3, 4) == None
    )  # function returns none (no list created only modified)


def test_add_at_index_mutate() -> None:
    """Tests that add at index mutates list correctly (use case)."""
    a: list[int] = [1, 2, 4, 5, 6]
    add_at_index(a, 3, 2)
    assert a == [1, 2, 3, 4, 5, 6]


def test_add_at_index_inputerror() -> None:
    """Tests that add at index raises error if index is out of range (edge case)."""
    a: list[int] = [1, 2, 4, 5, 6]
    with pytest.raises(IndexError):  # use pytest to check for raised error
        add_at_index(
            a, 3, 8
        )  # error should be raised since index = 8 is out of range (longer than list)
