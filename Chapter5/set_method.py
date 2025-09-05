# len() method is used in set,dictionary, string,list,tuple.
s={1,2,3,4,5,5,5}


print(s.add(6))  # add() method adds an element to the set.if the element is already present, it will not add the element and will ignore it.
print(s)
print(len(s))  # len() method returns the number of elements in the set.

print(s.remove(5))  # remove() method removes the specified element from the set.if the element is not present, it raises a KeyError.
print(s)

print(s.pop())  # pop() method removes and returns an arbitrary (random element delete) element from the set.if the set is empty, it raises a KeyError.
print(s)

print(s.clear())  # clear() method removes all elements from the set.
print(s)

