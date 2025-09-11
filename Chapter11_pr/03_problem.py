# problem 3: Use the property decorator to change the increment percentage of the employee class to 20% if the salary after increment is 280.8
# and also use the property decorator to get the salary after increment


class Employee:
    salary = 234
    increment = 20
    
    @property
    def salary_after_increment(self):
        return (self.salary+self.salary*(self.increment/100))
    
    @salary_after_increment.setter
    def salary_after_increment(self, salary):
        self.increment=((salary/self.salary)-1)*100
         
e=Employee()
# print(e.salary_after_increment)  # here we are accessing the method as an attribute without using
e.salary_after_increment=280.8  # here we are setting the value to the method as an attribute without using ()
print(e.increment)

