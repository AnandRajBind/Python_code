s1={1,44,58,69,78}
s2={1,2,3,4,5,6,7,8,9,10,44,58}


# in the union consider all the elements from both sets, but ignore the duplicates.
print(s1.union(s2))  # union() method returns a new set that contains all elements from both sets, without duplicates.



# in the intersection consider the only common elements.
print(s1.intersection(s2))  # intersection() method returns a new set that contains only the elements that are present in both sets.