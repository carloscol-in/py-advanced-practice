"""
Sets practice & theory

    - Set's elements are immutable.
    - Sets are sorted by default.    
"""


# see how it deletes duplicates
my_set = {1,2,3,3,5}
print(my_set)

# you can only pop first element from a set
my_set.pop()
print(my_set)

# you can append another set to your set
my_set.update({4,6})
print(my_set)
my_set.update([7, 10])
print(my_set)

# you can use discard and remove to delete specific items from your set
# but discard can ignore non existing values, on the other hand,
# remove will throw an error
my_set.discard(7) # will delete 7
my_set.discard(7)  # won't do anything
my_set.remove(10)  # will delete 10
try:
    my_set.remove(10) # will raise KeyError
except KeyError as e:
    print('It threw KeyError.')

# clean completely your set
my_set.clear()
print(my_set)