# types of functions    
# 1. Built-in functions Examples: print(), len(), type(), range()
# 2. User-defined functions Examples: avg(), greet()

# function with parameters and arguments
# parameters are the names used when defining a function, while arguments are the actual values passed to the function when calling it.


def greet(name, ending="Thankyou"): # function definition with parameters and default parameter
    print("Hello, welcome to functions in Python!"+ name)
    print(ending)
    
greet("Anand", "Thanks") # function call with arguments
greet("Raj") # function call with one argument, second argument takes default value