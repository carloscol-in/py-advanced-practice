"""
Sets practice and reference"""

def remove_duplicates(array):
    return list(set(array))

assert remove_duplicates([1,1,1,2,3,3,5,5,5]) == [1,2,3,5]