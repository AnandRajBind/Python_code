
# when a child class becomes a parent class for another child class.
# जब एक चाइल्ड क्लास किसी अन्य चाइल्ड क्लास के लिए पैरेंट क्लास बन जाती है

class Employee:
    def __init__(self):
        print("Constructor of Employee")
    a=10
    
class Programmer(Employee):
    def __init__(self):
        print("Constructor of Programmer")
    b=20
    
    
class Manager(Programmer):
    def __init__(self):
        super().__init__() # calls the constructor of Programmer class
        print("Constructor of Manager")
    c=30

o = Employee()
print(o.a) # Prints the a attribute
 
# p = Programmer()
# print(p.a, p.b) # Prints the a attribute
 

# m = Manager()
# print(m.a, m.b, m.c) # Prints the a attribute















