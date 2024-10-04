def contains(needle: int, haystack: list[int]) -> bool:
    idx: int = 0
    while idx < len(haystack):
        if haystack[idx] == needle:
            return True
        else:
            idx += 1
    return False


print(contains(23, [1, 2, 3, 4]))
print(contains(3, [1, 2, 3, 4]))


x: list[float] = [1.0, 2.0]
y: list[float] = [3.0, 4.0]
y = x
x[0] = 3.0

print(x)
print(y)
