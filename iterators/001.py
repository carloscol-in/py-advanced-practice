"""
Every iterable has to be made an iterator first before
trying to loop through them, for example.

An iterable is every element that is divisible in unique
elements that can be looped through.
"""

# Making iterator from iterable
mylist = [1,2,3,4,5]
myiter = iter(mylist)

print(next(myiter))

# iterating through iterator
while True:
    try:
        el = next(myiter)
        print(el)
    except StopIteration:
        break

# for loops are sugar syntax of the code block presented above
for el in mylist:
    print(el)