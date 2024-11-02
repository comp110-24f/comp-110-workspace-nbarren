from CQs.cq09.point import Point

"""CQ09 - Intro to OOP; defining objects and calling methods."""

new_point: Point = Point(2, 3)
new_point.scale_by(2)
print(new_point.x)
print(new_point.y)
point2: Point = new_point.scale(2)
print(new_point.x)
print(new_point.y)
print(point2.x)
print(point2.y)
