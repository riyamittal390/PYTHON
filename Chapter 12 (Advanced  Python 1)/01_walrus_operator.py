# Walrus operator(:=), introduced in Python 3.8, allows us to assign values to variables as part of an expression. 
# This operator, named for its resemblance to the eyes and tusks of a walrus, is officially called the "assignment expression"

if (n := len([1, 2, 3, 4, 5])) > 4:
    print (f"List is too long ({n} elements, expected <= 3)")