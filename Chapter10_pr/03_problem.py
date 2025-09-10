# problem 3 
class Demo:
    a=4
    
    
obj=Demo() # object creation
print(obj.a) # prints class attribute because instance attribute is not present

obj.a=5 # instance attribute is set to 5
print(obj.a) # prints the  instance attribute because instance attribute is present
print(Demo.a) # prints the class attributes. class attribute is not changed
