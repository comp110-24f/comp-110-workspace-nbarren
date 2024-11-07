"""File to define a river class!"""

__author__ = "730744691"

from exercises.ex07.fish import Fish
from exercises.ex07.bear import Bear


class River:
    """Class to define river objects with day and list of fish and bears."""

    day: int
    fish: list[Fish]
    bears: list[Bear]

    def __init__(self, num_fish: int, num_bears: int):
        """Function to define new fish objects."""
        """New River with num_fish Fish and num_bears Bears"""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Function that removes bears and fish who are old."""
        new_bears: list[Bear] = []  # empty list to add surviving bears to
        for animal in self.bears:  # loops through every bear in the list of river bears
            if 5 >= animal.age:
                new_bears.append(animal)  # animal will survive if age is 5 or less
        self.bears = new_bears  # replaces river bear list with surviving bear list
        new_fish: list[Fish] = []  # sets up new list for surviving fish
        for animal in self.fish:
            if 3 >= animal.age:
                new_fish.append(animal)  # animal will survive if age is 3 or less
        self.fish = new_fish  # replaces river fish list with surviving fish list
        return None

    def bears_eating(self):
        """Function to simulate bears eating fish."""
        for animal in self.bears:  # loops through each bear in list of river bears
            if (
                len(self.fish) >= 5
            ):  # must be at least five fish in list for bears to eat
                animal.eat(
                    3
                )  # animal is a bear class so this calls the bear eat function with num fish = 3
                self.remove_fish(
                    3
                )  # three fish must be removed since they were ate (self is a fish object so remove fish method is called from fish class)
        return None

    def check_hunger(self):
        """Function to remove bears who are starving."""
        hungry_bears: list[Bear] = []  # sets up new list for surviving bears
        for animal in self.bears:  # loops through each bear in river bear list
            if animal.hunger_score >= 0:
                hungry_bears.append(
                    animal
                )  # bear added to surviving list if their hunger score is at least 0
        self.bears = hungry_bears  # replaces river bear list with surviving bear list
        return None

    def repopulate_fish(self):
        """Function to simulate rish reproduction."""
        num_new_fish: int = (
            len(self.fish) // 2
        ) * 4  # determines num of fish added to river fish list
        num: int = 1  # set up to use in while loop
        while (
            num_new_fish >= num
        ):  # will loop thru num times of num of new fish being added
            new_fish: Fish = Fish()  # creates new fish object
            self.fish.append(new_fish)  # adds new fish object to river fish list
            num += 1
        return None

    def repopulate_bears(self):
        """Function to stimulate bear reproduction."""
        new_bear_num: int = (
            len(self.bears) // 2
        )  # determines how many bears will be added to list
        num: int = 1  # set up to use in while loop
        while new_bear_num >= num:  # stops running when correct num of bears are added
            new_bear: Bear = Bear()  # creates new bear object
            self.bears.append(new_bear)  # adds new bear object to river bear list
            num += 1
        return None

    def view_river(self):
        """Function to display day and number of fish and bears in river."""
        print(
            f"~~~ Day {self.day}: ~~~"
        )  # use f-strings to print the changing day value for self
        print(
            f"Fish Population: {len(self.fish)}"
        )  # self.fish refers to a list type so you can take the length to get the num of fish
        print(f"Bear population: {len(self.bears)}")
        return None

    def one_river_day(self):
        """Simulate one day of life in the river"""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """Function to simulate one week by calling the one day function seven times."""
        day: int = 1  # set up day 1 variable to model each day of the week
        while 7 >= day:  # will run through seven days
            self.one_river_day()  # calls one day function already defined in class
            day += 1
        return None

    def remove_fish(self, amount: int):
        """Function to remove a certain number of fish from the beginning of the list."""
        idx: int = amount - 1  # must decrease amount by one since idx starts at 0
        while (
            idx >= 0
        ):  # must loop through list backwards to remove front first fish and not mess with objects assigned at idxs
            self.fish.pop(idx)  # removes fish at that idx from river fish list
            idx -= 1
        return None
