"""File to define Fish class."""

__author__ = "730744691"


class Fish:
    """Class to define Fish objects with age."""

    age: int

    def __init__(self):
        """Defines new Fish objects."""
        self.age = 0
        return None

    def one_day(self):
        """Function to adjust fish age after one day."""
        self.age += 1  # adds one to fish object age (self refers to the specific fish)
        return None
