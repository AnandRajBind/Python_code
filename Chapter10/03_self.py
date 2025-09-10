# defining a class using class keyword
class Employee:
     salary=10000 # class attribute
     language="Python"
     
    #  self is a reference to current object.
    # self refers to the instance of the class.it is automatically passed with a function call from an object.
     def getInfo(self):
         print(f"salary is {self.salary} and language is {self.language}")

# some times we do not want to use self or instance variable inside a method. we can use static method like this.
     @staticmethod
     def greet():
        print("Hello Good Morning")
        

# object creation
rohan=Employee()
rohan.language="Java" # instance attribute prfresence over class attribute
print(rohan.language, rohan.salary  )
rohan.getInfo()
rohan.greet()
Employee.getInfo(rohan) # we can also call method using class name by passing object as
# Employee.getInfo() # TypeError: getInfo() missing 1 required positional argument: 'self'
