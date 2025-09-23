# 

# by using slice operator to reverse a string

# slicing is perform existing data like: string, list, tuple
list=["StAndrews", 1] # type list
collegeName="StAndrews" # type string
# slicing is perform  only orderd data (string, list, tuple)
# syntax of slice operator
# variable[start:end:step]. Here start is inclusive and end is exclusive 
# collegeName(8:0:-1) # swerdnAt
print(collegeName[::-1]) # swerdnAtS
print(type(collegeName[::-1])) # jis type ka data hoga wahi return hoga like: list, tuple, string

# set and dictionary are unordered data type so we can't use slicing on them

# range(start, end, step) method is used to generate a sequence of numbers 
