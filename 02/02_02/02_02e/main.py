''' 
Problem Statement: Compute the average number of pets each student 
has in a given class. 
'''

student_pet_count_list = [0, 1, 0, 2, 1, 1, 4, 0, 0, 0, 3, 2, 1, 3, 0, 2, 2, 4]

# use UPPER_CASE_NAMES for constants (values that do not
# change), and lower_cap_names for variables (values that may 
# change)
NUM_OF_STUDENTS = len(student_pet_count_list)
print(f"NUM_OF_STUDENTS: {NUM_OF_STUDENTS}")

# average = sum / number of items
SUM = 0

for INDIVIDUAL_PET_COUNT in student_pet_count_list:
    SUM += INDIVIDUAL_PET_COUNT

print(f"SUM: {SUM}")

AVERAGE_PET_COUNT = SUM / NUM_OF_STUDENTS
print(f"AVERAGE_PET_COUNT: {AVERAGE_PET_COUNT}")