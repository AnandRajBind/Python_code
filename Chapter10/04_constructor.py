# defining a class using class keyword
class Employee:
     salary=10000 # class attribute
     language="Python"
     
     def __init__(self, name, salary, language): # constructor or dunder method. it is automatically called when an object of the class is created. it is started and ended with double underscore.
         
        self.name=name
        self.salary=salary
        self.language=language
        print("I am a constructor")
     
     def getInfo(self):
         print(f"salary is {self.salary} and language is {self.language}")

     @staticmethod
     def greet():
        print("Hello Good Morning")


# object creation
obj=Employee("Rohan", 20000, "Java") # object creation will call constructor
# rohan.language="Java" # instance attribute prfresence over class attribute
print(rohan.name, rohan.language, rohan.salary)

rohan.greet()