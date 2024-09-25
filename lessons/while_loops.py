def loop(stop: int) -> None:
    condition: bool = True
    num_loops: int = 0
    while condition:
        print(num_loops)
        num_loops = num_loops + 1
        if num_loops >= stop:
            condition = False


# loop(stop=2)


def characters(msg: str) -> None:
    index: int = 0
    while index < len(msg):
        print(msg[index])
        index = index + 1


characters(msg="Howdy")
