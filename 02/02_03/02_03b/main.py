''' 
Problem Statement: Compute the average number of pets each student 
has in a given class. 
'''

student_pet_count_list = [0, 1, 0, 2, 1, 1, 4, 0, 0, 0, 3, 2, 1, 3, 0, 2, 2, 4]

# use UPPER_CASE_NAMES for constants (values that do not
# change), and lower_cap_names for variables (values that may 
# change)
num_of_students = len(student_pet_count_list)
print(f"num_of_students: {num_of_students}")

# average = sum / number of items
sum = 0

for individual_pet_count in student_pet_count_list:
    sum += individual_pet_count

print(f"sum: {sum}")

average_pet_count = sum / num_of_students
print(f"average_pet_count: {average_pet_count}")