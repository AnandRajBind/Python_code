s1={1,2,3}
s2={3,4,5}


# in the union consider all the elements from both sets, but ignore the duplicates.
print(s1.union(s2))  # union() method returns a new set that contains all elements from both sets, without duplicates.



# in the intersection consider the only common elements.
print(s1.intersection(s2))  # intersection() method returns a new set that contains only the elements that are present in both sets.

# subset 

print(s1.issubset(s2))  # issubset() method returns True if all elements of the set are present in the specified set, otherwise it returns False.

print(s1.issuperset(s2))  # issuperset() method returns True if all elements of the specified set are present in the set, otherwise it returns False.

