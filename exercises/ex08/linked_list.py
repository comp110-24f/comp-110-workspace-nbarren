from __future__ import annotations

"""EX08 -- Linked List and Recursive Functions."""

__author__ = "730744691"


class Node:
    """Class to create a node object with a value and a next node to create a linked list."""

    value: int
    next: Node | None

    def __init__(self, value: int, next: Node | None):
        """Magic method function to construct a Node object."""
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
    if (
        head.next is None
    ):  # if there is not another node (aka head.next) then this node is the last value (base case)
        return head.value
    else:
        return last(
            head.next
        )  # recursively calls last function until base case is reached (last value)


def value_at(head: Node | None, index: int) -> int:
    """Function to return the value of a linked list at a specific index."""
    if (
        head is None
    ):  # function cannot be called is head is none (there is no values in list)
        raise IndexError("Index is out of bounds on the list.")
    if (
        index == 0
    ):  # will be reached once recursive function is called the correct number of times
        return head.value
    else:
        return value_at(
            head=head.next, index=(index - 1)
        )  # decrease index, will keep calling until index is 0 and correct head.value is returned


print(value_at(Node(10, Node(20, Node(30, None))), 1))


def max(head: Node) -> int:
    """Function to return the greatest value of a linked list."""
    if head is None:
        raise ValueError("Cannot call max with None.")
    if (
        head.next is None
    ):  # will return last value in the linked list as the max and then return it to be compared with the other values (reach base case)
        return head.value
    if head.value > max(
        head.next
    ):  # this head.value will become the new max if its greater than all the other values later in the linked list
        return head.value
    else:
        return max(
            head.next
        )  # will recursively call the max function until base case (end value) is reached


print(max(Node(10, Node(20, Node(30, None)))))
print(max(Node(10, Node(30, Node(20, None)))))
print(max(Node(30, Node(20, Node(10, None)))))
# print(max(None))


def linkify(items: list[int]) -> Node | None:
    """Function to create a linked node list out of a int list."""
    if items == []:
        return (
            None  # if the list is empty then no node can be returned (so return none)
        )
    else:
        return Node(
            items[0], linkify(items[1:])
        )  # recursively calls linkify until items list is empty and base case is reached and constructed the linked list
    return None


print(linkify([1, 2, 3]))
print(linkify([]))
print(linkify([2, 3, 4, 5, 6]))


def scale(head: Node | None, factor: int) -> Node | None:
    """Function to scale all values in a linked list by a specific factor."""
    if (
        head is None
    ):  # cannot scale any values if there is no values so return none; will be the end of the recursive call when base case is reached (when theres no next value)
        return None
    else:
        return Node(
            (head.value * factor), scale(head.next, factor)
        )  # recursively calls scale until base case is reached and all values have been scaled


print(scale(linkify([1, 2, 3]), 2))
