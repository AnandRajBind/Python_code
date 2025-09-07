# function is a group of statements that perform a specific task
# function is a block of code which only runs when it is called

 

# The part containing the exact set of instructions which are executed during the function call is called function definition
def avg(): # function definition
    a=int(input("Enter first number: "))
    b=int(input("Enter second number: "))
    c=int(input("Enter third number: "))
    average=(a+b+c)/3
    print(average)
    return average # return statement

a=avg() # function call: Whatever we want to call a function, we use function name followed by parentheses.


print("The average is:", a)