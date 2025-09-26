# This is a simple function definition and call in Python.
def display():
    print("Function in Training/function.py")
    
display()

# Function: A function is a block of code which only runs when it is called. You can pass data, known as parameters, into a function. A function can return data as a result.

# Function return Types:
# takes somthing return something 1, 1
def display(a,b):
    return a+b
print(display(10,20))


# takes somthing return nothing
# takes nothing return something ...
# takes nothing return nothing


num1=int(input("Enter num1 value"))
num2=int(input("Enter num2 value"))
num3=int(input("Enter num3 value"))


def gretestValue(num1,num2, num3):
    if(num1>=num2) and (num1>=num3):
        return num1
    elif(num2>=num1) and (num2>=num3):
        return num2
    else:
        return num3
print(f"Gretest value is: {gretestValue(num1,num2,num3)}")
