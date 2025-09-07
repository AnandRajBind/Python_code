#  Recursion function: A function that calls itself is known as a recursive function.
#  Example: Factorial of a number

def factorial(n):
    if n==1 or n==0:
        return 1
    else:
        return n*factorial(n-1)
    
num=int(input("Enter a number to find factorial: "))
print(f"The factorial of {num} is {factorial(num)}")