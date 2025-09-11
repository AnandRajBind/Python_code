class Employee:
    company = "Google"
    name ="Default name"
    def show(self):
        print(f"The name of the company is {self.company} and the salary is {self.company}")
        
class Coder:
    language= "Python" 
    def printLanguage(self):
        print(f"The language is {self.language}")

#  multiple inheritance
class Programmer(Employee, Coder):
    company= "Python"
    def showLanguage(self):
        print(f"The name is {self.company} and he is good with {self.language} language")

a= Employee() # object of employee class
b= Programmer() # object of programmer class

b.showLanguage() # calling method of programmer class
b.show()
b.printLanguage() # calling method of coder class

