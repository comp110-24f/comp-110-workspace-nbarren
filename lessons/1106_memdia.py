def jump(x: int) -> int:
    """A strange function."""
    if x == 1:
        x = around(x - 2)
    print("jump")
    return x + 1


def around(x: int) -> int:
    """A nonsensical function."""
    while x > 0:
        return jump(x - 1)
    print("around")
    return 109


x: int = around(2)
print(x)


class Vector:
    x: int
    y: int

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)


v1: Vector = Vector(2, 3)
v2: Vector = Vector(4, 5)
v3: Vector = v1 + v2
print(v1)
print(v2)
print(v3)
