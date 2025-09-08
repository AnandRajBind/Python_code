# problem 4 : replace a word in a file with some other word
word="Donkey"

with open("file.txt","r") as f:
    content=f.read()
    newContent=content.replace(word,"$%#@!")
    



with open("file.txt","w") as f:
    f.write(newContent)