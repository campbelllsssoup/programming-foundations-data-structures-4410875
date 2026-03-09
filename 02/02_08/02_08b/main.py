my_list = [1, 7, 3]

# task: sort the numbers in ascending order
# print(sorted(my_list)

# task: sort the numbers in descending order
# print(sorted(my_list, reverse=True))

# note: the sorted method will result in an ascending order by default
student_grades = [('Sarah', 89), ('Rebecca', 82), ('Matt', 91)]

# in this example, when tuples are the elements being sorted, the function will 
# result in an alphabetical sort. By defualt, the function will use the first 
# element, to determine how to sort the list

# print(sorted(student_grades))

# override the functionality by using a lambda function to define how to sort
# the list
# task: sort the list by grade (second el in the tuple) in descending order
reverse_grade_sorted = sorted(student_grades, key=lambda x:x[1], reverse = True)
print(reverse_grade_sorted)

# note: sorting is computationally expensive!!!

# note: the number of comparisons that must be performed to sort, depends on 
# which sorting algorithm you use

# note: if you need to search inside of a list often, it may be a good idea
# to sort it, in order to save time.