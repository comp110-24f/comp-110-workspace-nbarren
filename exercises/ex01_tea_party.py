"""Exercise to help plan the cost of a tea party."""

__author__ = "730744691"


def main_planner(
    guests: int,
) -> None:
    """Function that gives the number of tea bags, treats, and the cost."""
    print(
        "A Cozy Tea Party for " + str(guests) + " People!"
    )  # must convert guests to a string value since ints can not be concantenated; guests is a local variable that can be assingned to the number of people parameter
    print("Tea Bags: " + str(tea_bags(people=guests)))  # convert int to str again
    print("Treats: " + str(treats(people=guests)))  # int to str
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )  # make call to tea_bags and treats within cost function since the cost function does not contain a parameter that can be assigned the local variable of guests


def tea_bags(people: int) -> int:
    """Function to compute the number of teas bags needed based on number of guests."""
    return people * 2


def treats(people: int) -> int:
    """A function to determine the number of treats needed based on the number of teas."""
    return int(
        tea_bags(people=people) * 1.5
    )  # must convert output to an int since the return type is an int, and you can't have a fraction of a treat (otherwise the function would give a float value)


def cost(tea_count: int, treat_count: int) -> float:
    """A function to compute the cost of the tea bags and treats combined."""
    return (0.50 * tea_count) + (
        0.75 * treat_count
    )  # will have to make a call to the tea_bags and treats funtion when evaluating the cost function to determine treat_count and tea_count


if __name__ == "__main__":
    main_planner(
        guests=int(input("How many guests are attending your tea party? "))
    )  # putting the input function after the int argument allows for users to input their own number of guests/their own value for the guests parameter
