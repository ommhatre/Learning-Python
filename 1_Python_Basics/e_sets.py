# Sets
# they are defined in curly brackets, and they are unordered, and also ignore duplicate values
# sets are there to just check if something exists in the set or not

set1 = {"math", "bio", "comp", "math"}
print(set1)

# sets are used to check if a value exists in the set
# this is called the membership test, and they do it more efficiently than lists and tuples

set2 = {"art", "history", "math", "design"}

# we can also use sets to check whats similar between two sets
print(set1.intersection(set2))

# and to check whats different
print(set1.difference(set2))

# to combine two sets
print(set1.union(set2))

# to creat an empty set
empty_set = set()