
# problem 7   if the names of 2 friendsare same. what will happen to the program in problem 6?


# ans: the value of the previous key will be replaced by the new value. 
d={} # empty dictionary
name=input("Enter friend name: ")
language=input("Enter favourite language: ")
d.update({name:language})
name=input("Enter friend name: ")
language=input("Enter favourite language: ")
d.update({name:language})
name=input("Enter friend name: ")
language=input("Enter favourite language: ")
d.update({name:language})
name=input("Enter friend name: ")
language=input("Enter favourite language: ")
d.update({name:language})

print(d)

# problem 8 if language of 2 friends are same. what will happen to the program in problem 6?

# ans: nothing will happen as keys are different

# problem 9  can youe change the values inside a list which is contained in set S?
s={1,2,3,4,[5,6] ,"Anand"} # set
# ans: no, because set can only contain immutable items. list is mutable. so it will give error





