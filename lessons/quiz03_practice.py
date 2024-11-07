class Course:
    name: str
    level: str
    prerequisites: list[str]

    def __init__(self):
        self.name = ""
        self.level = 0
        self.prerequisites = []

    def is_valid_course(self, prereq: str) -> bool:
        if prereq in self.prerequisites and self.level >= 400:
            return True
        return False


def find_courses(courses: list[Course], prereq: str) -> list[str]:
    course_list: list[str] = []
    for item in courses:
        if (prereq in item.prerequisites) and (item.level >= 400):
            course_list.append(item)
    return course_list


class Car:
    make: str
    model: str
    year: int
    color: str
    mileage: float

    def __init__(self, make: str, model: str, year: int, color: str, miles: float):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.mileage = miles

    def update_mileage(self, miles: float):
        self.mileage = self.mileage + miles
        return None

    def display_info(self):
        print(
            f"make: {self.make}, model: {self.model}, year: {self.year}, color: {self.color}, mileage: {self.mileage}"
        )
        return None


def calculate_depreciation(vehicle: Car, depreciation_rate: float) -> float:
    return vehicle.mileage * depreciation_rate


new_car: Car = Car("Ford", "Escape", 2013, "Black", 80000.0)
new_car.update_mileage(120.5)
new_car.display_info()
print(calculate_depreciation(new_car, 0.98))


class HotCocoa:
    has_whip: bool
    flavor: str
    marshmallow_count: int
    sweetness: int

    def __init__(self, whip: bool, flav: str, marsh: int, sweet: int):
        self.has_whip = whip
        self.flavor = flav
        self.marshmallow_count = marsh
        self.sweetness = sweet

    def mallow_adder(self, mallows: int):
        self.marshmallow_count += mallows
        self.sweetness = self.sweetness * (2 * mallows)
        return None

    def __str__(self):
        if self.has_whip:
            return f"A {self.flavor} cocoa with whip, {self.marshmallow_count} marshmallows, and level {self.sweetness} sweetness."
        if not self.has_whip:
            return f"A {self.flavor} cocoa without whip, {self.marshmallow_count} marshmallows, and level {self.sweetness} sweetness."


def order_cost(drinks: list[HotCocoa]) -> float:
    cost: float = 0.0
    for drink in drinks:
        if drink.has_whip:
            cost += 2.50
        if not drink.has_whip:
            cost += 2.00
    return cost


my_order: HotCocoa = HotCocoa(False, "vanilla", 5, 2)
my_order.has_whip = True
my_order.mallow_adder(2)
viktoryas_order: HotCocoa = HotCocoa(True, "peppermint", 10, 2)
print(order_cost([my_order, viktoryas_order]))
print(my_order)


class TimeSpent:
    name: str
    purpose: str
    minutes: int

    def __init__(self, name: str, purpose: str, minutes: int):
        self.name = name
        self.purpose = purpose
        self.minutes = minutes

    def add_time(self, increase: int):
        self.minutes += increase
        return None

    def __add__(self, added_minutes: int):
        return TimeSpent(self.name, self.purpose, self.minutes + added_minutes)

    def reset(self) -> int:
        num_min: int = self.minutes
        self.minutes = 0
        return num_min

    def __str__(self):
        hours: int = self.minutes // 60
        minu: int = self.minutes % 60
        return (
            f"{self.name} has spent {hours} hours and {minu} minutes on {self.purpose}."
        )


def most_by_purpose(times: list[TimeSpent], purpose: str) -> str:
    most_name: str = ""
    most_time: int = 0
    for time in times:
        if time.purpose == purpose and time.minutes > most_time:
            most_name = time.name
            most_time = time.minutes
    return most_name


a: TimeSpent = TimeSpent("Alyssa", "studying", 5)
b: TimeSpent = TimeSpent("Alyssa", "doom scrolling", 100)
c: TimeSpent = TimeSpent("Vrinda", "studying", 200)
print(most_by_purpose([a, b, c], "studying"))
print(c)
print(a)
print(b)
