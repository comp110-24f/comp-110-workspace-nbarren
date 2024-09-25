"""EX02 - Chardle - A step toward Wordle."""

__author__ = "730744691"


def input_word() -> str:
    word: str = str(
        input("Enter a 5-character word: ")
    )  # must convert the int input into a str for it to be concatenated
    if len(word) != 5:
        print("Error: Word must contain 5 characters.")
        exit()  # exit funtion should be put here so that no value is returned if the word does not have 5 characters
    return word


def input_letter() -> str:
    letter: str = str(
        input("Enter a single character: ")
    )  # must convert int input value into a str for it to be concatenated
    if len(letter) != 1:
        print("Error: Character must be a single character.")
        exit()  # exit function allows for no value to be returned when it is not a single letter
    return letter


def contains_char(word: str, letter: str) -> None:
    print(
        "Searching for " + letter + " in " + word
    )  # will use local variables from input_letter and input_word
    count: int = 0
    if letter == word[0]:
        print(letter + " found at index 0")
        count = (
            count + 1
        )  # count will only be increased when if block is entered (aka letter is present)
    if (
        letter == word[1]
    ):  # must use multiple if statements (not elif) since each index needs to be evaluated and not skipped over
        print(letter + " found at index 1")
        count = count + 1
    if letter == word[2]:
        print(letter + " found at index 2")
        count = count + 1
    if letter == word[3]:
        print(letter + " found at index 3")
        count = count + 1
    if letter == word[4]:
        print(letter + " found at index 4")
        count = count + 1
    if count == 0:
        print("No instances of " + letter + " found in " + word)
    elif (
        count == 1
    ):  # can use elif statements since count will only match one value (do not need to evaluate every statement)
        print("1 instance of " + letter + " found in " + word)
    elif count == 2:
        print("2 instances of " + letter + " found in " + word)
    elif count == 3:
        print("3 instances of " + letter + " found in " + word)
    elif count == 4:
        print("4 instances of " + letter + " found in " + word)
    elif count == 5:
        print("5 instances of " + letter + " found in " + word)


def main() -> (
    None
):  # allows main() to be used to call contains_char, input_word, and input_letter
    contains_char(word=input_word(), letter=input_letter())


if __name__ == "__main__":  # allows function to run without being called first
    main()
