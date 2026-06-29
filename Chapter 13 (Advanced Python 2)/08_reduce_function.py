# Reduce applies a rolling computation to sequential pair of elements.

# Syntax:
# from functools import reduce
# val = reduce (function, list1)


from functools import reduce

listt = [1, 2, 4, 3, 7]

def sum(a, b):
    return a + b

print(reduce(sum, listt))         # Output : 17

