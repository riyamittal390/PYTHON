# Class
# A Class is a blueprint for creating object.

class Employee:
    name = "Riya"        # name, salary, language are class attributes bcoz they belong to the class
    language = "Python"
    salary = 1200000

riya = Employee()
print(riya.name, riya.language)