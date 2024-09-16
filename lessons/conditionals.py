"""Conditional Practice."""


def less_than_10(num: int) -> None:
    dub: int = num * 2
    dub = dub - 1
    print(dub)
    if num < 10:
        print("Small number!")
    else:
        print("Big number!")
    print("Have a nice day!")


less_than_10(num=7)


# print(less_than_10(num=11))
# print(less_than_10(num=3))


def check_first_letter(word: str, letter: str) -> str:
    if word[0] == letter:
        return "match!"
    else:
        return "no match!"


# print(check_first_letter(word="monday", letter="m"))
# print(check_first_letter(word="happy", letter="p"))
