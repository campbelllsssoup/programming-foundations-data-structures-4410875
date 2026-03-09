# Tuples are immutable array-like structures

# tuple = (r, g, b) RGB color values
# tuple = (x, y) lat-long coordinate

point = (5, 2)

x = point[0]
y = point[1]

# create a function that returns the area and perimeter of a square
# this is just for an example to show you how to use a tuple. normally you 
# may prefer to use a dictionary to return this, and label the keys 'area' 
# and 'label'. Returning a  dictionary makes more sense here, generally.

def calculate_square_properties(side_length):
    area = side_length * side_length
    perimeter = 4 * side_length
    return (area, perimeter)

result = calculate_square_properties(5)
print(f"Area: {result[0]}")
print(f"Perimeter: {result[1]}")