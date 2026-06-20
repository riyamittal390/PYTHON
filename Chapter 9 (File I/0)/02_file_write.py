# st = "Hi Riya, You are amazing"
# f = open("myfile.txt", "w")
# f.write(st)
# f.close()






# f = open("file.txt")
# lines = f.readlines()               # it will read all lines
# print(lines, type(lines))





f = open("file.txt")
lines = f.readline()               # it will read only one line
print(lines, type(lines))