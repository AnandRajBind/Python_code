#  *******************************readlines() method***********************************

f=open('file.txt')
lines=f.readlines() # readlines() method reads all lines of file and returns a list of lines.
print(lines, type(lines))
f.close()



# ****************************readline() method***********************************

#  readline
f=open('file.txt')
line1=f.readline() # readline() method reads one line of the file at a time.
print(line1, type(line1))
line2=f.readline()
print(line2)

line3=f.readline()
print(line3)

line4=f.readline()
print(line4 == "") # if there is no more line to read, it returns empty string.
f.close() 


# ***************************readline() using while loop***************************
f=open('file.txt')
line= f.readline()

while(line != ""):
    print(line)
    line=f.readline()
    
f.close()