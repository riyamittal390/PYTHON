# The 'enumerate' function adds counter to an iterable and returns it.

# l = [43, 86, 46, 63, 689]
# index = 0
# for item in l:
#     print(f"The item number {index} is {item}")
#     index += 1





# Using enumerate function

l = [43, 86, 46, 63, 689]
for index, item in enumerate(l):
    print(f"The item number at index {index} is {item}")