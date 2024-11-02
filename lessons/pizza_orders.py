"""Practicing object oritented programming and creating new objects."""


class Pizza:
    gluten_free: bool
    size: str
    num_toppings: int

    def __init__(self, gf_input: bool, size_input: str, num_toppings_input: int):
        self.gluten_free = gf_input
        self.size = size_input
        self.num_toppings = num_toppings_input

    def price(self) -> float:
        price: float = 0.0
        if self.size == "small":
            price += 5.25
        else:
            price += 7.50
        price = price + 0.25 * self.num_toppings
        if self.gluten_free:
            price += 1
        return price


my_pizza: Pizza = Pizza(False, "large", 2)
print(my_pizza.gluten_free)
print(my_pizza.size)
print(my_pizza.num_toppings)
print(my_pizza.price())
