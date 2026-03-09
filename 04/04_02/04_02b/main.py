# set - a collection of unique items, unordered, no duplicate items
# group things with a common property
# order doesn't matter; we don't want to retreive data - no index or key
# testing if a piece of data is a member in the set
# does the set contain a given number, character, or string

# implementation:
# similar to dictionaries, but the key is the value

primary_colors = set(["red", "blue", "yellow"])
color = "green"
if color in primary_colors:
    print(color + " is a primary color")
else:
    print(color + " is not a primary color")

letters = set(['a', 'b'])
letters.add('c')
print(letters) #=> {'c', 'a', 'b'}
letters.add('c')
# adding another 'c' will not alter the set
print(letters) #=> {'c', 'a', 'b'}