# set#frozenset freezes the set, you may not add new values
primary_colors = frozenset(["red", "blue", "yellow"])

if "blue" in primary_colors:
    print("Blue in the set!")

# returns AttributeError: 'frozenset' object has no attribute 'add'
primary_colors.add("green")