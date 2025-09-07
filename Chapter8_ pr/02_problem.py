#  problem 2: Write a Python program to convert temperature in Fahrenheit to Celsius degree.
def far_to_cel(f):
    return 5*(f-32)/9

f=int(input("Enter temperature in Fahrenheit: "))
c=far_to_cel(f)    

print(f"{round(c,2)}°C")

# problem 3: Write a Python program to print the following string in a specific format (see the output).how to avoid new line in print statement

print("a")
print("b")
print("c", end="")
print("d", end="")
print("e")

# problem 4: Write a Python program to calculate the sum of first n natural numbers using recursion.

def sum(n):
    if(n==1):
        return 1
    else:
        return n+sum(n-1)

print(sum(5))

# problem 5: Write a Python program to print the following pattern using recursion.
'''
*****
****
***
**
*
'''
def pattern(n):
    if(n==0):
        return
    else:
        print("*"*n)
        pattern(n-1)

pattern(5)



        


