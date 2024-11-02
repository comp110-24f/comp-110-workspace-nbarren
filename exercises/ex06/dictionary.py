"""EX06 - Dictionary Utility Functions."""

__author__ = "730744691"


def invert(input: dict[str, str]) -> dict[str, str]:
    """Function that switches keys and values."""
    invert_dict: dict[str, str] = {}  # setup empty dict to assign values and keys to
    for key in input:  # loops thru each key-value pair in input dict
        if (
            input[key] in invert_dict
        ):  # ensures that when inverted, duplicate keys cannot exist
            raise KeyError("duplicate keys")
        invert_dict[input[key]] = key  # reassigns key to value and value to key
    return invert_dict


def favorite_color(input: dict[str, str]) -> str:
    """Function that returns the favorite color of a group of people."""
    most_popular: str = str()  # setup empty str to hold most popular color
    max_count: int = 0  # setup max count to be associated with most popular color
    for key in input:
        count: int = 0
        for elem in input:  # compares each key in input to every other key in input
            if input[key] == input[elem]:
                count += 1  # count increases if value of key is equal to value of elem
        if (
            count > max_count
        ):  # will only be evaluated if count exceeds previous max count
            max_count = count
            most_popular = input[
                key
            ]  # reassigns popular color to the current one that has max count
    return most_popular


def count(input: list[str]) -> dict[str, int]:
    """Function that returns the count of each elem in an input list."""
    count_dict: dict[str, int] = {}  # setup empty dict to transfer list values
    for elem in input:
        if elem in count_dict:  # checks if list elem is already a key in dict
            count_dict[elem] += 1
        else:  # will be evaluated if elem is not already a key in dict
            count_dict[elem] = (
                1  # creates a new key in dict assigned value of list elem
            )
    return count_dict


def alphabetizer(input: list[str]) -> dict[str, list[str]]:
    """Function that returns each elem of an input list in a new list based on its beginning letter."""
    new_dict: dict[str, list[str]] = {}  # setup empty dict to assign key-value pairs
    for elem in input:
        if (
            elem[0].lower() in new_dict
        ):  # elem will be added to an already existing list if the first letter of that word already exists as a key
            new_dict[elem[0].lower()].append(elem)
        else:  # creates new list with elem and assigned key of first letter of word
            new_dict[elem[0].lower()] = [elem]
    return new_dict


print(alphabetizer(["cat", "apple", "boy", "angry", "bad", "car"]))
print(alphabetizer(["Python", "Sugar", "Turtle", "party", "table"]))


def update_attendance(input: dict[str, list[str]], day: str, student: str) -> None:
    """Function that returns lists for each days attendance record."""
    if (
        day in input and student not in input[day]
    ):  # must check that student is not already in list (name will not be a repeat)
        input[day].append(
            student
        )  # student is added to attendance list that already exists for that day
    elif (
        day not in input
    ):  # if day is not already a key, a new key-pair value needs to be created
        input[day] = [student]


attendance_log: dict[str, list[str]] = {
    "Monday": ["Vrinda", "Kaleb"],
    "Tuesday": ["Alyssa"],
}
update_attendance(attendance_log, "Tuesday", "Vrinda")
update_attendance(attendance_log, "Wednesday", "Kaleb")
print(attendance_log)
