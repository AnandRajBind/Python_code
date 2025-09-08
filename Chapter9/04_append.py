
st="append the text in the file using append mode of file handling in python"

f=open('file.txt','a') # 'a' is used to open file in append mode.
f.write('\n') # to write in new line
print(f.write(st)) # it returns number of characters written in the file.
f.close()

# + mode are used for both reading and writing file (updating file). 
# rb will open file in binary mode for reading.
# rt will open file in text mode for reading.


