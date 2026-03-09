def find_second_smallest(my_list):
    if len(my_list) == (0 or 1):
        return None
    sorted_arr = sorted(my_list)
    return sorted_arr[1]

# DONE!: task: return the second smallest item, 3
# DONE!: if the list contains no items, or 1 item return None

print(find_second_smallest([5, 8, 3, 2, 6]))