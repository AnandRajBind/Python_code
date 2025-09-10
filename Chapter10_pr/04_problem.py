# problem 4 add a static method to the calculator class which greets the user with a message "Hello Good Morning"

class Calculator:
    def __init__(self, num):
        self.num=num

    def square(self):
        print(f"The square of {self.num} is {self.num*self.num}")
        
    def cube(self):
        print(f"The cube of {self.num} is {self.num*self.num*self.num}")
        
    def squareroot(self):
        print(f"The squareroot of {self.num} is {self.num**1/2}")
    
     @staticmethod
    def greet():
        print("Hello Good Morning")

a = Calculator(4)
a.greet()
a.square()
a.cube()
a.squareroot()
