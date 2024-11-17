from __future__ import annotations


class Node:
    value: int
    next: Node | None

    def __init__(self, value: int, next: Node | None):
        self.value = value
        self.next = next

    def __str__(self) -> str:
        """Represent a Node object as a str."""
        rest: str = ""
        if self.next is None:
            rest = "None"
        else:
            rest = str(self.next)
        return f"{self.value} -> {rest}"


two: Node = Node(2, None)
one: Node = Node(1, two)
courses: Node = Node(110, Node(210, Node(301, None)))


def to_str(head: Node | None) -> str:
    """Represent a Linked List as a str."""
    if head is None:
        return "None"
    else:
        rest: str = to_str(head.next)
        return f"{head.value} -> {rest}"


def last(head: Node) -> int:
    """Return the last value of a linked list."""
    print(head.value)
    if head.next is None:
        return head.value
    else:
        return last(head.next)


def recursive_range(start: int, end: int) -> str:
    """Building a linked list recursively."""
    if start == end:
        return None
    else:
        return Node(start, recursive_range((start + 1), end))


print(recursive_range(110, 112))
