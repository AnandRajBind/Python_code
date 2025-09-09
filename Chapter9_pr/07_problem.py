# problem 7: Read the log file line by line and print the line number where the word 'python' is found. If the word is not found, print a message saying so.

with open('log.txt',)as f:
    lines=f.readlines()

lineno=1
for line in lines:
    if('python' in line):
        print(f'python is present in line No.{lineno}')
        break
    lineno+=1
else:
    print('python is not present in the log file.')
    
    