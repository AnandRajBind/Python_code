with open('log.txt',)as f:
    content=f.read()
    
if 'python' in content.lower():
    print('python is present in the log file.')
else:
    print('python is not present in the log file.')