# problem1 write a program to create a dictionary of hindi words with values as their english translation. provide user with an option to look up a word.


words = {
    
    "madad": "help",
    "paani": "water",
    "bhook": "hunger",
    "pyas": "thirst",
}
word=input("Enter a hindi word to get its english translation: ")

print(words[word]) # it will give error if word not found in dictionary

# problem 2 write a program to create an empty set and take 8 numbers as input from the user and add them to the set and print the set.

s=set() #emptyset

num=int(input("Enter a number: "))
s.add(num)
num=int(input("Enter a number: "))
s.add(num)
num=int(input("Enter a number: "))
s.add(num)
num=int(input("Enter a number: "))
s.add(num)
num=int(input("Enter a number: "))
s.add(num)
num=int(input("Enter a number: "))
s.add(num)
num=int(input("Enter a number: "))
s.add(num)
num=int(input("Enter a number: "))
s.add(num)

print(s)

# problem 3 write a program to demonstrate that sets do not allow duplicate values.
s=set()
s.add(20)
s.add("20")

print(s) # it will print both 20 and "20" because one is integer and other is string


# problem 4  what will be the length of the following set 
s=set()
s.add(20)
s.add(20.0)
s.add("20")  

print(len(s)) # it will print 2 because 20 and 20.0 are considered same in set

# problem 5  s={}
# What is the type of s?
# Ans: it is empty dictionary not set
s={}
print(type(s))


# problem 6 write a program to take input from user and create a dictionary of friends and their favourite languages. (take 4 friends)
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

# problem 7  





























































































 