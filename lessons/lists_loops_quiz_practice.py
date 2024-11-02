"""List practice for quiz02."""

x: list[int] = [9, -1, 8, 5]
y: list[str] = ["cat", "dog", "turtle", "elephant", "fish"]
z: list[str] = ["z"]


def print_int_elems(input: list[int]) -> None:
    idx: int = 0
    while idx < len(input):
        print(input[idx])
        idx += 1


# print_int_elems(x)


def print_str_elems(input: list[str]) -> None:
    idx: int = 0
    while idx < len(input):
        print(input[idx])
        idx += 1

    # print_str_elems(y)
    # print_str_elems(z)

    # for elem in x:
    print(elem)
    # for elem in y:
    print(elem)
    # for elem in z:
    print(elem)


for idx in range(0, len(x)):
    print(x[idx])
for idx in range(0, len(y)):
    print(y[idx])
for idx in range(0, len(z)):
    print(z[idx])

my_list: list[int] = list()
my_list = [8, 0, 3, -1]
print(my_list)
my_list.pop(2)
print(my_list)
dog: int = my_list[2]
print(dog)
print(len(my_list))
my_list[0] = 0
print(my_list)


def sum(input: list[int]) -> int:
    sum: int = 0
    for num in input:
        sum += num
    return sum


print(sum(my_list))
