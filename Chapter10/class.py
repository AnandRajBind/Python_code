# defining a class using class keyword
class Employee:
     salary=10000 # class attribute
     language="Python"
    
# object creation
rohan=Employee()
rohan.name="Rohan"
print(rohan.name, rohan.salary, rohan.language)

aman=Employee()
aman.name="Aman" # instance attribute or object attribute
print(aman.name, aman.salary, aman.language)

# here name is object attribute whereas salary and language are class attributes as they directly belong to class