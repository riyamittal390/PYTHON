# __init__() is a specialmethod which is first run as soon as the object is created.
# __init__() method is also known as constructor.
# It takes self-argument and can also take further arguments.

class Employee:
    def __init__(self, name):
        self.name = name
    def getSalary(self):
        ...

riya = Employee("Riya")