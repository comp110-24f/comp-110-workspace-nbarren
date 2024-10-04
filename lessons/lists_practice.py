my_numbers: list[float] = list()

my_numbers.append(1.5)

game_points: list[int] = [102, 86, 94, 102]
game_points[1] = 72

print(my_numbers)
print(game_points)
print(len(game_points))


def display(input: list[int]) -> None:
    idx: int = 0
    while idx < len(input):
        print(input[idx])
        idx += 1


display(game_points)
