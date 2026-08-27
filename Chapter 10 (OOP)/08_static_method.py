# We use static method when we need a function that does not use the self parameter.

class Employee:
    language = "Python"
    salary = 1200000

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good morning")

riya = Employee()
riya.greet()
riya.getInfo()