# __init__() is a special method which is first run as soon as the object is created.
# __init__() method is also known as constructor.
# It takes self-argument and can also take further arguments.
# Methods in python starting with '__' are called "Dunder methods".
# Dunder methods are the methods which are automatically called.
# Only __init__ dunder method is called automatically, not all methods.

class Employee:
    def __init__(self, name):
        self.name = name
    def getSalary(self):
        ...

riya = Employee("Riya")