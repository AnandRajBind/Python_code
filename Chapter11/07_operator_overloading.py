# operators in python can be overloaded using dunder methods
#

class Number:
    def __init__(self, n):
        self.n=n
        
    def __add__(self, num):
        return self.n + num.n
    
n=Number(5)
m=Number(10)

print(n + m)  # this will call n.__add__(m) and return 15 here we are overloading the + operator using __add__ method
# similarly we can overload other
