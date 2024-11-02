from __future__ import annotations

"""CQ09 - Intro to OOP; defining the class Point and methods."""


class Point:
    x: float
    y: float

    def __init__(self, x_init: float, y_init: float) -> None:
        self.x = x_init
        self.y = y_init

    def scale_by(self, factor: int) -> None:
        self.x = self.x * factor
        self.y = self.y * factor

    def scale(self, factor: int) -> Point:
        new_point: Point = Point(self.x, self.y)
        new_point.x = self.x * factor
        new_point.y = self.y * factor
        return new_point
