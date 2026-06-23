# A class method is a method which is bounded to the class and not the object of the class.
# @classmethod decorator is used to create a class method.

class Employee:
    a = 1

    @classmethod
    def show(cls):
        print(f"The class attribute of 'a' is {cls.a}")

e = Employee()
e.a = 45
e.show()                    # If we do self.a, then it will print 45 and if we will do cls.a, then it will print 1.