import math


class Pizza:
    size: str
    extra_cheese: bool
    toppings: int

    def __init__(self):
        self.size = "medium"
        self.extra_cheese = False
        self.toppings = 0

    def get_price(self):
        price: float = 11.00
        if self.size == "large":
            price = 13.00
        if self.extra_cheese:
            price += 1.00
        price += self.toppings * 0.75
        return price


my_pizza: Pizza = Pizza()
my_pizza.toppings = 1
print(f"${my_pizza.get_price()}")

ur_pizza: Pizza = Pizza()
ur_pizza.size = "large"
print(f"Extra cheese? {ur_pizza.extra_cheese}")
print(f"${ur_pizza.get_price()}")
print(my_pizza)


class Circle:
    radius: float

    def __init__(self, r: float):
        self.radius = r

    def area(self) -> float:
        area: float = math.pi * (self.radius) ** 2
        return area


circ: Circle = Circle(r=2.0)
print(circ.area())


class Rectangle:
    width: float
    height: float

    def __init__(self, w: float, h: float):
        self.width = w
        self.height = h

    def area(self) -> float:
        area: float = self.width * self.height
        return area


rect: Rectangle = Rectangle(w=4.0, h=5.5)
print(rect.area())
