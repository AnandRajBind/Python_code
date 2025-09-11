class Employee:
    company = "Google"
    def show(self):
        print(f"The name of the company is {self.name} and the salary is {self.salary}")
        
# without inheritance

# class Programmer(Employee):
#     company = "Fiverr"
#     def show(self):
#         print(f"The name of the company is {self.company} and the salary is {self.salary}")
        
#     def showLanguage(self):
#         print(f"The name is {self.name} and he is good with {self.language} language")
        

# with inheritance


class Programmer(Employee):
    company= "Python"
    def showLanguage(self):
        print(f"The name is {self.name} and he is good with {self.language} language")
        
        
a= Employee()
b= Programmer()

print(a.company, b.company)