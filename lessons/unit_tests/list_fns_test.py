from lessons.unit_tests.list_fns import get_first, remove_first, get_and_remove_first


def test_get_first() -> None:
    fruits: list[str] = ["apples", "oranges", "bananas"]
    assert get_first(fruits) == "apples"


def test_remove_first_ret_val() -> None:
    """test that remove first returns none."""
    fruits: list[str] = ["apples", "oranges", "bananas"]
    assert remove_first(fruits) == None


def test_remove_first_behavior() -> None:
    fruits: list[str] = ["apples", "oranges", "bananas"]
    remove_first(fruits)
    assert fruits == ["oranges", "bananas"]


def test_get_first_edge_case() -> None:
    """Test that get_first works with empty list."""
    list: list[str] = []
    assert get_first([]) == ""
