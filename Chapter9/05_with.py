f=open("file.txt")
print(f.read())
f.close()


# no need to use f.close() as with statement automatically closes the file.
 
with open("file.txt") as f:
    print(f.read())

# you dont have to explicitly close the file when using with statement.