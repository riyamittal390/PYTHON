# Map applies a function to all the items in an input_list.

# Syntax:
# map(function, input_list)


listt = [1, 2, 3, 4, 5]
square = lambda x : x * x
sqList = map(square, listt)
print(list(sqList))             # Output : [1, 4, 9, 16, 25]
