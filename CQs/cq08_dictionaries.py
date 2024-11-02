def find_eligible(names: list[str], ages: list[int]) -> dict[str, int]:
    """Find the names and ages of all ppl old enough to rent a car!"""
    if len(names) != len(ages):
        raise ValueError("Diff lengths.")
    eligible_ppl: dict[str, int] = {}
    for idx in range(0, len(names)):
        if ages[idx] >= 25:
            eligible_ppl[names[idx]] = ages[idx]
    return eligible_ppl


names: list[str] = ["Allan", "Ken", "Barbie"]
ages: list[int] = [23, 26, 25]
renters: dict[str, int] = find_eligible(names, ages)
print(renters)

if "Ken" in renters:
    renters.pop("Ken")

print(renters)
