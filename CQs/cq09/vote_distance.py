class Point:
    x: float
    y: float

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def dist_from_origin(self) -> float:
        return (self.x**2 + self.y**2) ** 0.5

    def translate_x(self, dx: float) -> None:
        self.x += dx

    def translate_y(self, dy: float) -> None:
        self.y += dy


class Line:
    start: Point
    end: Point

    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end

    def get_length(self) -> float:
        length: float = ((end.x - start.x) ** 2 + (end.y - start.y) ** 2) ** 0.5
        return length

    def get_slope(self) -> float:
        slope: float = (end.y - start.y) / (end.x - start.x)
        return slope


start: Point = Point(2.0, 1.0)
end: Point = Point(7.0, 5.0)
vote: Line = Line(start, end)
print(vote.get_length)
