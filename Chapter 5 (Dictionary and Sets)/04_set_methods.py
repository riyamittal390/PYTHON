s = {1, 5, 321, 6, 6, 6, 6, "Riya"}
# print(s)                   // Output : {321, 1, 'Riya', 5, 6}
# print(type(s))               // Output : <class 'set'>

s.add(566)
# print(s)                  // Output : {321, 1, 5, 6, 566, 'Riya'}

# print(len(s))               // Output : 6

s.remove(6)
# print(s)                      // Output : {321, 1, 'Riya', 5, 566}

s.pop()
# print(s)                       // Output : {1, 5, 566, 'Riya'}

# print(s.clear())                 // Output : None

s1 = {1, 4, 45, 6}
s2 = {4, 32, 21, 98}
# print(s1.union(s2))                // Output : {32, 1, 98, 4, 21, 6, 45}
# print(s1.intersection(s2))           // Output : {4}
