# Python lists are containers to store a set of values of any data type.
# A list can be indexed just like a string.
# Unlike strings, lists are mutable.

friends = ["Apple", "Orange", 5, 342.25, False, " Aakash"]
# print(friends[4])                 // Output : False

friends[2] = "Riya"
# print(friends[2])                 // Output : Riya
# print(friends[1:4])                 // Output : ['Orange', 'Riya', 342.25]

friends.append("ABC")
# print(friends)              Output : ['Apple', 'Orange', 'Riya', 342.25, False, ' Aakash', 'ABC']
