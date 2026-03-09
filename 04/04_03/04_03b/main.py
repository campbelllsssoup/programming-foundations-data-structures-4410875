set_A = {10, 20, 30, 40, 50}
set_B = {30, 40, 50, 60, 70}

# set#union
# combine the contents of both sets by using the union operation
union_set = set_A.union(set_B)

# set#intersection, remove the elements in set_A that aren't presesnt in 
# set_B
intersection_set = set_A.intersection(set_B)

# set#difference: remove the elements in set_A that also exist in set_B and 
# return the results
difference_set = set_A.difference(set_B)

# set#difference method: remove the elements in set_A that also exist in set_B
difference_set_BA = set_B.difference(set_A)
print(symmetric_difference_set)

# set#symmetric_difference returns the elements unique to both sets
symmetric_difference_set = set_A.symmetric_difference(set_B)
print(symmetric_difference_set)