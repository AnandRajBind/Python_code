# A class metod is a method that is bound to the class and not the object of the class. 

class Employee:
     a=10
     
     @classmethod # decorator to define a class method
     def show(cls):
         print(f"The class attribute of a is {cls.a}")
         

e = Employee()
e.a=45 # this will create an instance attribute a for object e
e.show() # The a is 10

