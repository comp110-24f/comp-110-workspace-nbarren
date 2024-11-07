"""File to define Bear class."""

__author__ = "730744691"


class Bear:
    """Class to define Bear objects with age and hunger."""

    age: int
    hunger_score: int

    def __init__(self):
        """To define a new bear object."""
        self.age = 0
        self.hunger_score = 0
        return None

    def one_day(self):
        """Function to change bear age and hunger after one day."""
        self.age += 1  # adds one day to the "self" bear
        self.hunger_score = (
            self.hunger_score - 1
        )  # will decrease bears hunger score each day
        return None

    def eat(self, num_fish: int):
        """Function to simulate bear eating fish."""
        self.hunger_score = (
            self.hunger_score + num_fish
        )  # hunger increases by the num fish ate
        return None
