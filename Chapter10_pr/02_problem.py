# problem 2 write a calculator program which can do square, cube and squareroot of a number using class and constructor.

class Calculator:
    def __init__(self, num):
        self.num=num

    def square(self):
        print(f"The square of {self.num} is {self.num*self.num}")
        
    def cube(self):
        print(f"The cube of {self.num} is {self.num*self.num*self.num}")
        
    def squareroot(self):
        print(f"The squareroot of {self.num} is {self.num**1/2}")
        

a = Calculator(4)
a.square()
a.cube()
a.squareroot()
