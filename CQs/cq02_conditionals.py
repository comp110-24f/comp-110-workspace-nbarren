"""Practice with conditionals, local variables, and user input."""

__author__ = "730744691"


def guess_a_number() -> None:
    secret: int = 7
    x: int = int(input("Guess a number: "))
    print("Your guess was " + str(x))
    if int(x) == 7:
        print("You got it!")
    elif int(x) < 7:
        print("Your guess was too low! The secret number is " + str(secret))
    elif int(x) > 7:
        print("Your guess was too high! The secret number is " + str(secret))
    return None


if __name__ == "__main__":
    guess_a_number()
