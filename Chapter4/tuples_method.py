
a= (10,20,33,4,5,6,10, False, True, "Hello") 
 
print(a)

no=a.count(10) # it will return the count of the element in the tuple
print(no)

index=a.index(5) # it will return the index of the first occurence of the element in the tuple
print(index)

# if the element is not present in the tuple it will give an error
# index=a.index(50)


my_tuples=(10,20,3,4,5)

repeated=my_tuples*3 # it will repeat the tuple 3 times
print(repeated)

print(2 in my_tuples) # it will return True if the element is present in the tuple else False