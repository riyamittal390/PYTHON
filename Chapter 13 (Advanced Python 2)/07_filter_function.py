# Filter creates a list of items for which the function returns true.

# Syntax:
# list(filter(function))


listt = [1, 2, 3, 4, 5]

def even(n):
    if (n % 2 == 0):
        return True
    return False

onlyEven = filter(even, listt)
print(list(onlyEven))               # Output : [2, 4]

