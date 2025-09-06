# first and second both if statement will be executed independently
a= int(input("Enter Your age:   "))

# first if statement
if(a%2==0):
    print("Your age is even")
    
# End of first if statement
    

# second if statement
if(a>=18):
    print("You can drive")
    print("You are an adult")
elif(a<0):
    print("You have entered invalid age")
 
else:
    print("You cannot drive")    
# end of second if statement

print("Thank you")