"""Examples of dictionary syntax with Ice Cream Shop order tallies."""

ice_cream: dict[str, int] = {
    "chocolate": 12,
    "vanilla": 8,
    "strawberry": 5,
}

print(len(ice_cream))
ice_cream["mint"] = 3
print(ice_cream)

print(ice_cream["chocolate"])
ice_cream["vanilla"] = 10
print(ice_cream)


def check_if_mint(ice_cream: dict[str, int]) -> None:
    if "mint" in ice_cream:
        print("There are " + str(ice_cream["mint"]) + " orders of mint ice cream!")
    else:
        print("There are no orders of mint")


check_if_mint(ice_cream=ice_cream)

# ice_cream.pop("strawberry")
# print(ice_cream)

for key in ice_cream:
    print(key)
for key in ice_cream:
    print(ice_cream[key])

print(ice_cream["pecan"])
