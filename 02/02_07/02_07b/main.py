# Linear Search a.k.a. sequential search

# walk through the array one-by-one, and return a result if you find a match
# "find_first" method
# It's time complexity is O(n)

# improve the speed by implementing a binary tree search O(log n) time
# - the speed will only improve if the array contains a certain amount of
# items and can be sorted in a certain amount of time
# -  quicksort || merge sort; then binary search 




my_list = [8, 5, 0, 3, 9, 7]
ITEM = 7

def search(item, arr):
    for el in arr:
        if el == item:
            return item
    return None

result_0 = search(ITEM, my_list) # returns 7; stores it in a var 'result_0'
result_1 = search(1, my_list) # returns None;  stores it in a var 'result_1'

print(f"result 0: {result_0}")
print(f"result 1: {result_1}")