
# when a child class becomes a parent class for another child class.
# जब एक चाइल्ड क्लास किसी अन्य चाइल्ड क्लास के लिए पैरेंट क्लास बन जाती है

class Employee:
    a=10
    
class Programmer(Employee):
    b=20
    
    
class Manager(Programmer):
    c=30
       

o = Employee()
print(o.a) # Prints the a attribute
# print(o.b) # AttributeError: 'Employee' object has no attribute 'b'

p = Programmer()
print(p.a, p.b) # Prints the a attribute
# print(p.c)  # AttributeError: 'Programmer' object has no attribute 'c'


m = Manager()

print(m.a, m.b, m.c) # Prints the a attribute
 













