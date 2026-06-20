# Self refers to the instance of the class. It is automatically passed with a function call from an object.

class Employee:
    language = "Python"
    salary = 1200000

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    def greet(Self):
        print("Good morning")

riya = Employee()
riya.greet()
riya.getInfo()