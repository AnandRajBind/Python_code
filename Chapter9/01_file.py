# A file is a data stored in a storage device. A python program can talk to the file by reading contents from it and writing contents to it.
# There are two types of files in python
# 1. Text files (.txt, .py, .csv, .html, .css, .js etc)
# 2. Binary files (.jpg, .png, .mp3, .mp4, .pdf etc)



f=open("file.txt")  # open function is used to open a file. it have two parameters first is file name and second is mode. by default mode is 'r' (read mode). another modes are 'w' (write mode).
# ex:- f=open("file.txt", "r")

data=f.read()  # read function is used to read the contents of the file.
print(data)
f.close()  # close function is used to close the file.