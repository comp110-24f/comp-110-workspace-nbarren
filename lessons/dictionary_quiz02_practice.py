"""Dictionary practice for quiz02."""

my_dictionary: dict[str, float] = {}

msg: dict[str, int] = {"Hello": 1, "Yall": 2}
print(msg["Yall"])
msg["Yall"] += 3
print(msg["Yall"])

ids: dict[int, str] = {100: "Alyssa", 200: "Carmine"}
# ids.pop(100)
# print(ids)

print(len(ids))

inventory: dict[str, int] = {"pens": 10, "notebooks": 5, "erasers": 8}
inventory["markers"] = 15
print(inventory)

prices: dict[str, float] = {"bread": 2.99, "milk": 1.99, "eggs": 3.49}
prices["milk"] = 2.50
print(prices)

scores: dict[str, int] = {"Alice": 85, "Bob": 90, "Charlie": 88}
for key in scores:
    print(key)


def sum(inp_dict: dict[str, int]) -> int:
    score_sum: int = 0
    for key in inp_dict:
        score_sum += inp_dict[key]
    return score_sum


total_score: int = sum(inp_dict=scores)
print(total_score)

fruit_count: dict[str, int] = {"apples": 5, "bananas": 8}
for key in fruit_count:
    print(f"{key}: {fruit_count[key]}")

first_dict: dict[str, int] = {"a": 1, "b": 2}
second_dict: dict[str, int] = {"c": 3, "d": 4}


def combine(one: dict[str, int], two: dict[str, int]) -> dict[str, int]:
    combo_dict: dict[str, int] = {}
    for key in one:
        combo_dict[key] = one[key]
    for key in two:
        combo_dict[key] = two[key]
    return combo_dict


combo_dict: dict[str, int] = combine(first_dict, second_dict)
print(combo_dict)

my_dict: dict[int, str] = {}
my_dict[8] = "eight"
my_dict[0] = "zero"
my_dict[3] = "three"
my_dict[-1] = "negative one"
my_dict.pop(3)
cat: str = my_dict[0]
print(len(my_dict))
my_dict[8] = "zero"


def sum_dict_keys(input: dict[int, str]) -> int:
    sum: int = int()
    for key in input:
        sum += key
    return sum


sum_value: dict[str, int] = {"returned_amount": sum_dict_keys(my_dict)}
print(sum_value)
