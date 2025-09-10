# problem 1 write a program to print name, salary, pin code and company of 2 programmers using class and constructor.
class Programmer:
    company="Microsoft" # class attribute
    def __init__(self, name, salary,pin):
        self.name=name
        self.salary=salary
        self.pin=pin
        
        
         
obj1=Programmer("Rohan", 10000, 1234)
print(obj1.name, obj1.salary, obj1.pin, obj1.company)
obj2=Programmer("Shubham", 20000, 5678)
print(obj2.name, obj2.salary, obj2.pin, obj2.company)
