"""EX03 - An exercise to create your own wordle game."""

__author__ = "730744691"


def input_guess(secret_word_len: int) -> str:
    """Function to obtain a guess of the correct length."""
    guess: str = input(
        f"Enter a {secret_word_len} character word: "
    )  # use f-string format f"..{}..."; input function allows user to enter guess
    while len(guess) != secret_word_len:
        guess = input(f"That wasn't {secret_word_len} chars! Try again: ")
    return guess


def contains_char(secret_word: str, char_guess: str) -> bool:
    """Function to check word for a guessed character."""
    assert (
        len(char_guess) == 1
    )  # makes sure that the char_guess is only one character (will produce error if not)
    idx: int = 0
    while len(secret_word) > idx:
        if secret_word[idx] == char_guess:
            return True  # when this value is returned, the function is exited (stops being evaluated once return statement is read)
        idx = idx + 1
    return False  # will only occur if if-block was never entered


def emojified(guess: str, secret_word: str) -> str:
    """Function to compare a users guess to the secret word."""
    assert len(guess) == len(
        secret_word
    )  # ensures that the users guess will be the same length as the secret word (error will occur if not)
    white_box: str = "\U00002B1C"
    green_box: str = "\U0001F7E9"
    yellow_box: str = "\U0001F7E8"
    idx: int = 0
    emoji_str: str = (
        str()
    )  # creates an empty string to add color blocks to as guess is analyzed
    while idx < len(guess):
        if guess[idx] == secret_word[idx]:
            emoji_str = (
                emoji_str + green_box
            )  # adds a green box to emoji str since letter is in correct position
        elif (
            contains_char(secret_word=secret_word, char_guess=guess[idx]) == True
        ):  # calling contains_char determines if the char is in the secret word at all -- will return True if it is
            emoji_str = (
                emoji_str + yellow_box
            )  # adds a yellow box to emoji str since letter is somewhere in the secret word
        else:  # char is not in word at all
            emoji_str = (
                emoji_str + white_box
            )  # adds a white box to emoji str since letter is not in the secret word
        idx += 1
    return emoji_str


def main(secret_word: str) -> None:
    """The entrypoint of the program and main game loop."""
    turn: int = 1  # will keep track of the users turn
    guess: str = ""  # empty str for user to enter guess
    won: bool = (
        False  # allows while statement to be evaluated when the user has not yet won (guessed the right word)
    )
    while turn <= 6 and not (
        won
    ):  # will be entered when user has turns left and they have not won yet
        print(f"=== Turn {turn}/6 ===")
        guess = input_guess(
            secret_word_len=len(secret_word)
        )  # calling secret_word_len allows user to enter their guess -- reassigns guess the value of their input
        print(
            emojified(guess=guess, secret_word=secret_word)
        )  # will give feedback to user in the form of the emoji str
        if guess == secret_word:  # will be entered if user has won
            print(f"You won in {turn}/6 turns!")
            won = True  # when won is reassigned this value the while block will no longer be entered again
        else:
            turn += 1
    if won:
        print(f"You have won in {turn}/6 turns!")  # printed when won == true
    else:
        print(
            "x/6 - Sorry, try again tomorrow!"
        )  # printed once user has ran out of turns and did not win


if __name__ == "__main__":
    main(secret_word="codes")
