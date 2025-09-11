# problem 2 create a class (animals) and use it to create another class (pets) using inheritance
# and then use it to create another class (dogs) using inheritance and add a method bark

class Animals:
    pass
    
class Pets(Animals):    
    pass

class Dogs(Pets):
    @staticmethod
    def bark():
        print(" bow bow")
        
d=Dogs()
d.bark()

