# problem 9 : Compare two files and print whether they are identical or not.    
with open('file.txt') as file:
    content1 = file.read()
    
    
with open('this_copy.txt') as file:
    content2 = file.read()

if(content1 == content2):
    print('Both files are identical.')
else:
    print('Files are not identical.')