
# problem 1: Create a list of marks by taking input from the user.
'''
fruits=[] # empty list 

f1=input("Enter fruit name: ")
fruits.append(f1)
f2=input("Enter fruit name: ")
fruits.append(f2)
f3=input("Enter fruit name: ")
fruits.append(f3)
f4=input("Enter fruit name: ")
fruits.append(f4)
f5=input("Enter fruit name: ")
fruits.append(f5)
f6=input("Enter fruit name: ")
fruits.append(f6)
f7=input("Enter fruit name: ")
fruits.append(f7)

print(fruits)

'''
# problem 2 : Create a list of marks by taking input from the user and display them in sorted manner (use sort() function)
marks=[] # empty list 

f1=int(input("Enter marks here: "))
marks.append(f1)
f2=int(input("Enter marks here: "))
marks.append(f2)
f3=int(input("Enter marks here: "))
marks.append(f3)
f4=int(input("Enter marks here: "))
marks.append(f4)
f5=int(input("Enter marks here: "))
marks.append(f5)
f6=int(input("Enter marks here: "))
marks.append(f6)
marks.sort() # this will sort the list in ascending order
print(marks)

# problem 3 : Create a tuple and try to change the value of one of its elements.

'''
a =(1,2,3,4,5,6, False, True, "Hello")
  
a[2]=10 # this will give an error as tuples are immutable
print(a)
'''

# problem 4 : Create a list of integers and find the sum of all the elements in the list.
l1=[5,6,8,4,5,4] # list of integers

print(sum(l1)) # this will give the sum of all the elements in the list

# problem 5 : Create a list of integers and find the largest element in the list.

a=(1,0,2,0,4,5,6,7,8,0,9) # tuple of integers

n=a.count(0) # this will count the number of 0 in the tuple
print("Number of 0 in the tuple is: ", n)