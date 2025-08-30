# write a python program to list all files and directories in a specified path.
import os
 
# Specify the directory you want to list

# directory_path = 'D:/Python_code/Chapter1_pr'
directory_path = '/' # root directory

# List all files and directories in the specified path

contents = os.listdir(directory_path)
print(contents)

# print ech file and directory name

for item in contents:
 print(item)
    