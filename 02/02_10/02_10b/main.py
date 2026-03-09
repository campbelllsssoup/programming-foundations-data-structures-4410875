def find_second_smallest(my_list):
    if len(my_list) < 2:
        return None
    sorted_arr = sorted(my_list)
    return sorted_arr[1]

# note: the sorted method uses the timsort algorithm
# timsort - hybrid sorting algorithm built using merge sort and insertion sort
#   - O(n log n) complexity

def find_second_smallest_v2(my_list):
    # list length check
    if len(my_list) < 2:
        return None
    # float('inf') is the highest possible number
    smallest = float('inf')
    second_smallest = float('inf')
    for num in my_list:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest:
            second_smallest = num
    return second_smallest


# task: create a custom algorithm to find the second smallest item
#   - iterate through the list, keeping track of the two smallest items

# time complexity of find_second_smallest_v2 is O(n), because we only have to 
# iterate through the list once

print(find_second_smallest_v2([5, 8, 3, 2, 6]))

# searching or sorting tuples or lists are not optimized for speed

