# Recursion is a function which calls itself.
# It is used to directly use a mathematical formula as function.

num = int(input("Enter a number : "))

def factorial(n):
    if (n == 0 or n == 1):
        return 1
    else:
        return n * factorial(n-1)

print(f"Factorial of {num} is : {factorial(num)}")
