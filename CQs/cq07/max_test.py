from CQs.cq07.find_max import find_and_remove_max

__author__ = "730744691"


def test_find_and_remove_max_return() -> None:
    """Tests that find and remove max returns correct max value."""
    a: list[int] = [1, 2, 3, 4, 3, 4, 2]
    assert find_and_remove_max(a) == 4


def test_find_and_remove_max_mutate() -> None:
    """Tests that find and remove max mutates input list properly."""
    a: list[int] = [1, 2, 3, 4, 3, 4, 2]
    find_and_remove_max(a)
    assert a == [1, 2, 3, 3, 2]


def test_find_and_remove_max_empty_input() -> None:
    """Tests that find and remove max returns correct max when list is only one value."""
    a: list[int] = [1]
    assert find_and_remove_max(a) == 1
