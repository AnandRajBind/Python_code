# problem 1 Write a function to find the greatest of three numbers.

def greatest(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    else:
        return c
   
print("The greatest number is:", greatest(10,200,30))    
    