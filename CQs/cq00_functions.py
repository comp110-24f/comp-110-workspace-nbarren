"""Challenge Questions 8/28"""

__author__ = "730744691"


def mimic(message: str) -> str:
    """Function that returns a message."""
    return message


mimic(message="hello")


def main() -> None:
    """Function prints the result of calling mimic."""
    return print(mimic(message=input("What is your message?")))


if __name__ == "__main__":
    main()
