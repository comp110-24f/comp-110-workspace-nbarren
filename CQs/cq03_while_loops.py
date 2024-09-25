"""While Loops Challenge Question 9/18"""

__author__ = "730744691"


def num_instances(phrase: str, search_char: str) -> int:
    count: int = 0
    index: int = 0
    while index <= len(phrase) - 1:
        if phrase[index] == search_char:
            count = count + 1
        index = index + 1
    return count


print(num_instances(phrase="HelloHeLloHEllo", search_char="e"))
print(num_instances(phrase="hello", search_char="l"))
print(num_instances(phrase="computer science", search_char="c"))
