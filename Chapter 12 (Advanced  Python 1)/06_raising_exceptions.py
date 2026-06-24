# We can raise custom exceptions using the 'raise' keyword in Python.

a = int(input("Enter a number : "))
b = int(input("Enter second number : "))

if(b == 0):
    raise ZeroDivisionError("Hey out program is now meant to divide numbers by zero")
else:
    print(f"The division a/b is {a/b}")