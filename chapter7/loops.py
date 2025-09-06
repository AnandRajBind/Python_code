# for loops 
# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

for i in range(1,6):
    print(i)


# while loops
i=1
while(i<6):
    print(i)
    i=i+1


# print all the names in the list using while loop
list=['Anand', 'Ravi', 'Kumar', 'Suresh',1, False]
i=0
while(i<len(list)):
    name=list[i]
    print(name)
    i=i+1       
    

# the range() function in python is used to generate a sequence of numbers. it can take one, two or three arguments.
# range(start, stop, step)
# start: the starting number of the sequence (inclusive). default is 0.
# step: the difference between each number in the sequence. default is 1. Example: 1 to 10 with step 3 (1,4,7,10)

for i in range(1,11,3):
    print(i)

# print all the numbers prsent in the list using for loop

list=[1,2,3,4,5]
for i in list:
    print(i)

# print all the numbers present  in the tuple using for loop

tuple=(1,2,3,4,5)
for i in tuple:
    print(i)
    
#  print all the characters present in the string using for loop

s="anand"
for i in s:
    print(i)
    

#  for loop with else
for i in list:
    print(i)
else:
    print("The loop is completed") # this else block will be executed after the loop is completed normally (not by break statement) 

