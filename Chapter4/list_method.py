friends = ["Anand", "Raj", "Bind", 1, 2, 3, True]

print(friends)
friends.append("NewFriend") # append method is used to add an element at the end of the list
print(friends)


l1=[15,85,5,85,8542,8,2,2,5]
l1.sort() # sort method is used to sort the list in ascending order
print(l1)

l1.reverse() # reverse method is used to reverse the list
print(l1)

l1.insert(2, 333) # insert method is used to insert an element at a particular index
print(l1)

l1.remove(85) # remove method is used to remove the first occurence of an element
print(l1)

print(l1.count(8542)) # count method is used to count the occurence of an element in the list


print(l1.pop(3)) # pop method is used to remove the last element of the list and return it. If index is provided it removes the element at that index
# print(l1)


