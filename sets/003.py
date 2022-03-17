"""
Operations with sets."""

my_set1 = {1,2,3}
my_set2 = {3,4,5}

# union
print('Union:', my_set1 | my_set2)

# intersection
print('Intersection:', my_set1 & my_set2)

# exclusion
print('Exclusion:', my_set1 ^ my_set2)

# difference
print('Difference:', my_set1 - my_set2)
print('Difference:', my_set2 - my_set1)