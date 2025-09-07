#  problem 8 Write a Python program to remove all occurrences of a specific word from a list.
def rem(l, word):
    n=[]
    for item in l:
        if not(item==word):
            n.append(item.strip(word))
    return n
l=["Anand", "Shubham", "Chandan", "Dinesh", "Rohan","an"]
# stripe method are used to remove extra spaces and specified characters from the beginning or end of a string.
print(rem(l, "an"))  # ['Anand', 'Chandan', 'Dinesh']

# problem 9 Write a Python program to print the multiplication table of a given number.

def multiply(n):
    for i in range(1,11):
        print(f"{n} x {i} = {n*i}")
        
multiply(5)