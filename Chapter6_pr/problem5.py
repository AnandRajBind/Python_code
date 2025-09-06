# problem 5 Write a program to check if a name is present in a list or not.

list=['Anand', 'Ravi', 'Kumar', 'Suresh']

name=input("Enter your name: ")

# whait is in keyword
# in keyword is used to check if a value is present in a sequence (list, tuple, string) or not. it returns True if the value is present otherwise False.
if (name in list): # in keyword
    print("Your name is present in the list")
else:
    print("Your name is not present in the list")


    