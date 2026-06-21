# Inheritance is a way of creating a new class from an existing class.






# Types of Inheritance

# 1. Single Inheritance
# Single inheritance occurs when child class inherits only a single parent class.

# 2. Multiple Inheritance
# Multiple inheritance occurs when the child class inherits from more than one parent classes.

# 3. Multilevel Inheritance
# Multilevel inheritance occurs when a child becomes a parent for another child class.





class Employee:
    company = "ITC"
    def show(self):
        print(f"The name of the employee is {self.name} and the salary is {self.salary}")

class Programmer(Employee):
    company = "ITC Infotech"
    def showLanguage(self):
        print(f"The name is {self.name} and he is good with {self.language} language")

a = Employee()
b = Programmer()

print(a.company, b.company)
