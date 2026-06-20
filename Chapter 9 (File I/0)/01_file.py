# The random-access memory is volatile, and all its contents are lost once a program terminates in order to persist the data forever, we use files.
# A file is data stored in a storage device. A python program can talk to the file by reading content from it and writing content to it.






# Types of Files
# There are 2 types of files:
# (a) Text Files (.txt, .c, etc)
# (b) Binary Files (.jpg, .dat, etc)






# Modes of Opening a File
# r - open for reading
# w - open for writing
# a - open for appending
# + - open for updating
# 'rb' - will open for read in binary mode
# 'rt' - will open for read in text mode





f = open("file.txt", "r")
data = f.read()
print(data)
f.close()