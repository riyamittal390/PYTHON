# Operators in Python can be overloaded using dunder methods.
# These ,ethods are called when a given operator is used on the objects.

# str__() is used to set what gets displayed upon calling str(obj)
# __len__() is used to set what gets displayed upon calling .__len__() or len(obj)

class Number:
    def __init__(self, n):
        self.n = n
    
    def __add__(self, num):
        return self.n + num.n
    
n = Number(1)
m = Number(7)

print(n + m)
