def get_first(list: list[str]) -> str:
    if len(list) == 0:
        return ""
    return list[0]


def remove_first(list: list[str]) -> None:
    list.pop(0)


def get_and_remove_first(list: list[str]) -> str:
    first_elem: str = list[0]
    list.pop(0)
    return first_elem


list1: list[str] = ["apple", "banana", "orange", "pear"]

print(get_and_remove_first(list=list1))
print(list1)
