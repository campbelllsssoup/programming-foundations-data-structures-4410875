# (Multidimensional lists)

# 2D array (a.k.a. matrix; table structure; [row][column])
# 3D array (cube-like structure; [depth][row][column])

seating_chart = [
    ["Sarah", "Claire", "Ben", "Taylor", "Eva"],
    ["Frankie", "George", "Lindsey", "Izzy", "Jack"],
    ["Katherine", "Lauren", "Mary", "Nathan", "Olive"],
    ["Chad", "April", "Matt", "Thomas", "Penny"]
]

print(f"seating_chart[2][1]: {seating_chart[2][1]}")

# 'enumerate function': built-in method that adds a counter to an iterable 
# (like a list, tuple, or string) and returns it as an enumerate object
# Syntax: enumerate(iterable, start=0 )

# 'enumerate object': an iterator that produces tuples containing the index 
# and the corresponding value from the iterable

# 'iterator': an object that enables sequential traversal through a collection 
# of elements, such as lists, arrays, or trees, without exposing the underlying 
# data structure

# 'syntax': set of rules that define how code must be structured and written 
# so that a computer can understand and execute it

# 'iterable': any object that can be looped over, such as in a for loop

# start counting at 1 for non-developers
for i, row in enumerate(seating_chart, start = 1):
    # print(f"row {i}, students {row}")
    for j, student_name in enumerate(row, start = 1):
        print(f"{student_name} is in row {i}, seat {j}")