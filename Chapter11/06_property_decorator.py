class Employee:
    
    a=10
    @classmethod
    def show(cls):
        print(f"The class attribute of a is {cls.a}")
    
    @property 
    def name(self):
        return f"{self.fname} {self.lname}"
    
    @name.setter
    def name(self, name):
        self.fname = name.split(" ")[0]
        self.lname = name.split(" ")[1]

e = Employee()
e.a = 45

e.name = "Anand raj"
print(e.fname, e.lname)
e.show()