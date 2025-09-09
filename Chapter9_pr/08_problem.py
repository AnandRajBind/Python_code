with open('file.txt', 'r') as file:
    content = file.read()


with open("this_copy.txt", 'w') as f:
    f.write(content)