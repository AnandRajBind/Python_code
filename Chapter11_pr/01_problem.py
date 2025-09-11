# problem 1 create a class (2-D vector) and it to create another class (3-D vector) using inheritance
# and use super() to access the parent class methods and attributes

class TwoDVector:
    def __init__(self, i, j):
        self.i = i
        self.j = j
    def show(self):
        print(f"The vector is {self.i}i + {self.j}j")
        
class ThreeDVector(TwoDVector):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k = k
    def show(self):
        print(f"The vector is {self.i}i + {self.j}j + {self.k}k")

obj=TwoDVector(1, 2)
obj.show()
obj2=ThreeDVector(1, 2, 3)
obj2.show()
# operators in python can be overloaded using dunder methods