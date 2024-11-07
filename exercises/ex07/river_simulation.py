"""File to run river simulation."""

__author__ = "730744691"

from exercises.ex07.river import (
    River,
)  # imports entire river class as well as the imported files from the river module

my_river: River = River(10, 2)  # creates new river object with 10 fish and 2 bears

my_river.view_river()  # use self.method to call rather than method(self)
my_river.one_river_week()
