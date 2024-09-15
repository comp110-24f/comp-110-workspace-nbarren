def greet(name: str) -> str:
    print(
        "Hello "
        + name
        + ", your name starts with an "
        + name[0]
        + " and ends with an "
        + name[len(name) - 1]
    )
    print("I'm so happy to see you " + name + "!")


def main() -> None:
    print(greet(name="Molly"))


main()
