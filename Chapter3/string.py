name='Anand'
 
 
nameShort=name[0:3]# start from index 0 to index 2. first index is include and last index 3 is not included
print(nameShort)
 
character=name[1] # first character of the string
print(character)    

# starting se index 0 se start hota hai
# ending se index -1 se start hota hai
print(name[-4: -1])
print(name[1:4])# corresponding positive index is 1 to 3

print(name[:4]) # start from index 0 to index 3
print(name[1:]) # start from index 1 to last index


# slicing with skip value
b="abcdefghijklmnopqrstuvwxyz"
print(b[1:9:4])# output is bf 

# other advanced slicing techniques
word="amazing"
word=word[:7] # same as word[0:7]
word=word[0:] # same as word[0:len(word)]